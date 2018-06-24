public class Solution {
    public int strStr(String haystack, String needle) {
        if (haystack == null || needle == null) {
            return -1;
        }
        int lenstr = haystack.length();
        int lensubstr = needle.length();;
        if (lenstr < lensubstr) {
            return -1;
        }
        int len = lenstr - lensubstr;
        for (int i=0; i <= len; i++) {
            int j;
            for (j=0; j < lensubstr; j++) {
                if (haystack.charAt(i+j) != needle.charAt(j)) {
                    break;
                }
            }
            if (j == lensubstr) {
                return i;
            }
        }
        return -1;
    }
}
