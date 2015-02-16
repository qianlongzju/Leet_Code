public class Solution {
    public int minDistance(String word1, String word2) {
        int[][] D = new int[word1.length()+1][word2.length()+1];
        for (int i=0; i <= word1.length(); i++) {
            D[i][0] = i;
        }
        for (int i=0; i <= word2.length(); i++) {
            D[0][i] = i;
        }
        for (int i=1; i <= word1.length(); i++) {
            for (int j=1; j <= word2.length(); j++) {
                if (word1.charAt(i-1) == word2.charAt(j-1)) {
                    D[i][j] = D[i-1][j-1];
                }
                else {
                    int min = D[i-1][j-1];
                    if (D[i][j-1] < min) {
                        min = D[i][j-1];
                    }
                    if (D[i-1][j] < min) {
                        min = D[i-1][j];
                    }
                    D[i][j] = min + 1;
                }
            }
        }
        return D[word1.length()][word2.length()];
    }
}
