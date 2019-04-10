class Solution {
public:
    int numDistinct(string S, string T) {
        int n = S.size();
        int m = T.size();
        int result[m+1][n+1];
        result[0][0] = 1;
        for (int i=1; i <= m; ++i) {
            result[i][0] = 0;
        }
        for (int j=1; j <= n; ++j) {
            result[0][j] = 1;
        }
        for (int i=1; i <= m; ++i) {
            for (int j=1; j <= n; ++j) {
                result[i][j] = result[i][j-1];
                if (S[j-1] == T[i-1]) {
                    result[i][j] += result[i-1][j-1];
                }
            }
        }
        return result[m][n];
    }
};
