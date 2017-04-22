public class Solution {
    public int lengthOfLongestSubstring(String s) {
        int n = s.length(), i = 0, j = 0, maxLen = 0;
        boolean[] exist= new boolean[256];
        for (int k = 0; k < 256; k++) {
            exist[k] = false;
        }
        while (j < n) {
            if (exist[s.charAt(j)]) {
                maxLen = Math.max(maxLen, j - i);
                while (s.charAt(i) != s.charAt(j)) {
                    exist[s.charAt(i)] = false;
                    i++;
                }
                i++;
            } else {
                exist[s.charAt(j)] = true;
            }
            j++;
        }
        return Math.max(maxLen, n - i);
    }
}
