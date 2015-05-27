public class Solution {
    public int minCut(String s) {
        int len = s.length();
        int[] f = new int[len+1];
        boolean[][] p = new boolean[len][len];
        // the worst case is cutting by each char
        for (int i = 0; i <= len; i++)
            f[i] = len - 1 - i; // 最后一个 f[len]=-1
        for (int i = 0; i < len; i++)
            for (int j = 0; j < len; j++)
                p[i][j] = false;
        for (int i = len - 1; i >= 0; i--) {
            for (int j = i; j < len; j++) {
                if (s.charAt(i) == s.charAt(j) && (j - i < 2 || p[i + 1][j - 1])) {
                    p[i][j] = true;
                    if ((f[j + 1] + 1) <  f[i])
                        f[i] = f[j+1] + 1;
                }
            }
        }
        return f[0];
    }
}
