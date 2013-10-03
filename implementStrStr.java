public class Solution {
    public String strStr(String haystack, String needle) {
        // Start typing your Java solution below
        // DO NOT write main() function
        if (haystack == null || needle == null) {
            return null;
        }
        int lenstr = haystack.length();
        int lensubstr = needle.length();;
        if (lenstr < lensubstr) {
            return null;
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
                return haystack.substring(i);
            }
        }
        return null;
        
    }
}
