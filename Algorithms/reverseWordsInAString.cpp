#include "leetcode.cpp"
class Solution {
public:
    void reverseWords(string &s) {
        // remove beginning spaces
        while (!s.empty() && s.front() == ' ')
            s.erase(s.begin());
        // remove ending spaces
        while (!s.empty() && s.back() == ' ')
            s.erase(s.end()-1);
        // if empty, do nothing
        if (s.empty())
            return ;
        // remove duplicate adjacent spaces
        for (int i=1; i < s.length();) {
            if (s[i] == ' ' && s[i-1] == ' ') {
                s.erase(i, 1);
            } else {
                i++;
            }
        }
        // reverse word
        int beginIndex = 0, endIndex = 0;
        while (endIndex <= s.length()) {
            if (s[endIndex] == ' ' || endIndex == s.length()) {
                for (int i=beginIndex, j=endIndex-1; i < j; i++, j--) {
                    int temp = s[i];
                    s[i] = s[j];
                    s[j] = temp;
                }
                beginIndex = endIndex + 1;
            }
            endIndex ++;
        }
        // reverse total string
        for (int i=0, j=s.length()-1; i < j; i++, j--) {
            int temp = s[i];
            s[i] = s[j];
            s[j] = temp;
        }     
    }
};

int main()
{
    string t = "the sky is blue";
    Solution s;
    s.reverseWords(t);
    cout << t << endl;
    t = "   a   b ";
    s.reverseWords(t);
    cout << t << endl;
    return 0;
}
