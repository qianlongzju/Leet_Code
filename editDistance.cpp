class Solution {
public:
    int minDistance(string word1, string word2) {
        // Start typing your C/C++ solution below
        // DO NOT write int main() function
        int D[word1.size()+1][word2.size()+1];
        for (int i=0; i <= word1.size(); i++) {
            D[i][0] = i;
        }
        for (int i=0; i <= word2.size(); i++) {
            D[0][i] = i;
        }
        for (int i=1; i <= word1.size(); i++) {
            for (int j=1; j <= word2.size(); j++) {
                if (word1[i-1] == word2[j-1]) {
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
        return D[word1.size()][word2.size()];
    }
};
