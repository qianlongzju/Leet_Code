public class Solution {
    public int lengthOfLongestSubstring(String s) {
        // Start typing your Java solution below
        // DO NOT write main() function
        int n = s.length();
        int i = 0, j = 0;
        int maxLen = 0;
        boolean[] exist= new boolean[256];
        for (int k=0; k < 256; k++) {
        	exist[k] = false;
        }
        while (j < n) {
            if (exist[s.charAt(j)]) {
            	if (j-i > maxLen) 
            		maxLen = j-i;
                while (s.charAt(i) != s.charAt(j)) {
                    exist[s.charAt(i)] = false;
                    i++;
                }
                i++;
                j++;
            } else {
                exist[s.charAt(j)] = true;
                j++;
            }
        }
        if (n-i > maxLen)
        	maxLen = n-i;
        return maxLen;
    }
}