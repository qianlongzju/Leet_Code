class Solution {
public:
    bool isPalindrome(string s) {
        for (int i=0, j=s.length()-1; i < j; ) {
            char a = s[i];
            char b = s[j];
            if (!isAlphaNumeric(a)) {
                i++;
                continue;
            }
            if (!isAlphaNumeric(b)) {
                j--;
                continue;
            }
            a = toLower(a);
            b = toLower(b);
            if (a != b) {
                return false;
            }
            i++;
            j--;
        }
        return true;
    }
    bool isAlphaNumeric(char c) {
        if ((c >= '0' && c <= '9') || (c >= 'a' && c <= 'z') || (c >= 'A' && c <= 'Z')) {
            return true;
        }
        return false;
    }
    char toLower(char c) {
        if (c >= 'A' && c <= 'Z') {
            c = c + 'a' - 'A';
        }
        return c;
    }
};
