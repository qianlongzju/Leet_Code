import java.util.*;
public class Solution {
    public boolean isValidSudoku(char[][] board) {
        // Start typing your Java solution below
        // DO NOT write main() function
        int[] num = new int[9];
        for (int i=0; i < 9; ++i) {
            for (int j=0; j < 9; ++j) {
                num[j] = 0;
            }
            for (int j=0; j < 9; ++j) {
                if (board[i][j] != '.') {
                    int digit = board[i][j] - '0';
                    if (num[digit-1] == 1) {
                      //  cout << "i: " << i << " j: " << j << endl;
                        return false;
                    } else {
                        num[digit-1] = 1;
                    }
                }
            }
            for (int j=0; j < 9; ++j) {
                num[j] = 0;
            }
            for (int j=0; j < 9; ++j) {
                if (board[j][i] != '.') {
                    int digit = board[j][i] - '0';
                    if (num[digit-1] == 1) {
                     //   cout << "j: " << j << " i: " << i << endl;
                        return false;
                    } else {
                        num[digit-1] = 1;
                    }
                }
            }
        }
        for (int i=0; i < 3; ++i) {
            for (int j=0; j < 3; ++j) {
                for (int k=0; k < 9; ++k) {
                    num[k] = 0;
                }
                for (int k=0; k < 3; ++k) {
                    for (int l=0; l < 3; ++l) {
                        if (board[i*3+k][j*3+l] == '.') {
                            ;
                        } else {
                            int digit = board[i*3+k][j*3+l] - '0';
                            if (num[digit-1] == 1) {
                    //            cout << "i: " << i << " j: " << j << " k: " << k << " l: " << l << endl;
                                return false;
                            } else {
                                num[digit-1] = 1;
                            }
                        }
                    }
                }
            }
        }
        return true;
    }
}
