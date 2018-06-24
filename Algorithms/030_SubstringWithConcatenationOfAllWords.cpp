#include "leetcode.h"
class Solution {
public:
    vector<int> findSubstring(string s, vector<string>& words) {
        vector<int> result;
        if (words.size() == 0)
            return result;
        int wordLength = words[0].size();
        int subLength = wordLength * words.size();
        int length = s.size();
        unordered_map<string, int>  wordCount, current;
        for (int i=0; i < words.size(); ++i)
            wordCount[words[i]] ++;
        for (int i=0; i <= length-subLength; i++) {
            current.clear();
            int j;
            for (j=0; j < words.size(); j++) {
                string word = s.substr(i + j*wordLength, wordLength);
                if (wordCount.find(word) == wordCount.end())
                    break;
                current[word] ++;
                if (current[word] > wordCount[word])
                    break;
            }
            if (j == words.size())
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

