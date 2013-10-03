class Solution {
public:
    char *strStr(char *haystack, char *needle) {
        // Start typing your C/C++ solution below
        // DO NOT write int main() function
        if (haystack == NULL || needle == NULL) {
            return NULL;
        }
        int lenstr = strlen(haystack);
        int lensubstr = strlen(needle);
        if (lenstr < lensubstr) {
            return NULL;
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
                return haystack + i;
            }
        }
        return NULL;
    }
};
