public class Solution {
    public String longestPalindrome(String s) {
        // Start typing your Java solution below
        // DO NOT write main() function
        int length = s.length();
        boolean[][] table = new boolean[length][length];
        int maxLen = 1;
        int maxIndex = 0;
        for (int i=0; i < length; i++) {       
            for (int j = 0; j < length; ++j)
                table[i][j] = false;
            table[i][i] = true;
            if (i+1 < length && s.charAt(i) == s.charAt(i+1)) {
                table[i][i+1] = true;
                maxLen = 2;
                maxIndex = i;
            }
        }
        for (int len=3; len <= length; len++) {
            for (int i=0; i < length-len+1; i++) {
                if (s.charAt(i) == s.charAt(i+len-1) && table[i+1][i+len-2] == true) {
                    table[i][i+len-1] = true;
                    maxLen = len;
                    maxIndex = i;
                }
            }
        }
        return s.substring(maxIndex, maxIndex+maxLen);  
    }
}