#include "leetcode.h"
class Solution {
public:
    vector<int> findSubstring(string S, vector<string> &L) {
        vector<int> result;
        int wordLength = L[0].size();
        int subLength = wordLength * L.size();
        int length = S.size();
        unordered_map<string, int>  wordCount, current;
        for (int i=0; i < L.size(); ++i)
            wordCount[L[i]] ++;
        for (int i=0; i <= length-subLength; i++) {
            current.clear();
            int j;
            for (j=0; j < L.size(); j++) {
                string word = S.substr(i + j*wordLength, wordLength);
                if (wordCount.find(word) == wordCount.end())
                    break;
                current[word] ++;
                if (current[word] > wordCount[word])
                    break;
            }
            if (j == L.size())
                result.push_back(i);
        }
        return result;
    }
};
int main() {
    Solution s;
    string S = "barfoothefoobarman";
    vector<string> L;
    L.push_back("foo");
    L.push_back("bar");
    vector<int> result = s.findSubstring(S, L);
    for (int i=0; i < result.size(); i++)
        cout << result[i] << " ";
    cout << endl;
    return 0;
}

