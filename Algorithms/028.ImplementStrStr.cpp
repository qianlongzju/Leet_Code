class Solution {
public:
    int strStr(string haystack, string needle) {
        if (needle == "") {
            return 0;
        }
        int lenstr = haystack.size();
        int lensubstr = needle.size();
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
