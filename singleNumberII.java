import java.util.*;
public class Solution {
    public int singleNumber(int[] A) {
        int n = A.length;
        int result = 0;
        for (int j=0; j < 32; ++j) {
            int tmp = 0;
            for (int i=0; i < n; ++i) {
                if ((A[i] & (1<<j)) != 0) {
                    tmp ++;
                }
            }
            result += (tmp%3) << j;
        }
        return result;
    }
}
