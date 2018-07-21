class Solution {
public:
    int strStr(char *haystack, char *needle) {
        if (haystack == NULL || needle == NULL) {
            return -1;
        }
        int lenstr = strlen(haystack);
        int lensubstr = strlen(needle);
        if (lenstr < lensubstr) {
            return -1;
        }
        int len = lenstr - lensubstr;
        for (int i=0; i <= len; i++) {
            int j;
            for (j=0; j < lensubstr; j++) {
                if (haystack[i+j] != needle[j]) {
                    break;
                }
            }
            if (j == lensubstr) {
                return i;
            }
        }
        return -1;
    }
};
