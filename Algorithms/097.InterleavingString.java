public class Solution {
    public boolean isInterleave(String s1, String s2, String s3) {
        int n = s1.length();
        int m = s2.length();
        boolean IL[][] = new boolean[n+1][m+1];
        for (int i=0; i <= n; ++i) {
            for (int j=0; j <= m; ++j) {
                IL[i][j] = false;
            }
        }
        if ((m+n) != s3.length())
            return false;
        for (int i=0; i <= n; ++i) {
            for (int j=0; j <= m; ++j) {
                if (i == 0 && j == 0)
                    IL[i][j] = true;
                else if (i == 0) {
                    if (s2.charAt(j-1) == s3.charAt(j-1))
                        IL[i][j] = IL[i][j-1];
                }
                else if (j == 0) {
                    if (s1.charAt(i-1) == s3.charAt(i-1))
                        IL[i][j] = IL[i-1][j];
                }
                else if (s1.charAt(i-1) == s3.charAt(i+j-1) && s2.charAt(j-1) != s3.charAt(i+j-1)) 
                    IL[i][j] = IL[i-1][j];
                else if (s2.charAt(j-1) == s3.charAt(i+j-1) && s1.charAt(i-1) != s3.charAt(i+j-1))
                    IL[i][j] = IL[i][j-1];
                else if (s1.charAt(i-1) == s3.charAt(i+j-1) && s2.charAt(j-1) == s3.charAt(i+j-1)) 
                    IL[i][j] = IL[i][j-1] || IL[i-1][j];
            }
        }
        return IL[n][m];
    }
}
