public class Solution {
    public int minDistance(String word1, String word2) {
        int[][] D = new int[word1.length()+1][word2.length()+1];
        for (int i=0; i <= word1.length(); i++)
            D[i][0] = i;
        for (int i=0; i <= word2.length(); i++)
            D[0][i] = i;
        for (int i=1; i <= word1.length(); i++) {
            for (int j=1; j <= word2.length(); j++) {
                D[i][j] = Math.min(D[i][j-1], D[i-1][j]) + 1;
                D[i][j] = Math.min(D[i][j], D[i-1][j-1] + (word1.charAt(i-1) == word2.charAt(j-1)? 0:1));
            }
        }
        return D[word1.length()][word2.length()];
    }
}
