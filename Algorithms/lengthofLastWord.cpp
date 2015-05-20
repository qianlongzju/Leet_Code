class Solution {
public:
    int lengthOfLastWord(string s) {
        int n = s.size();
        if (n == 0) {
            return 0;
        }
        bool wordBegin = false;
        int count = 0;
        for (int i=n-1; i >= 0; i--) {
            if (s[i] != ' ') {
                if (wordBegin) {
                    count++;
                }
                else {
                    wordBegin = true;
                    count++;
                }
            }
            else {
                if (wordBegin) {
                    return count;
                }
            }
        }
        return count;
    }
};
