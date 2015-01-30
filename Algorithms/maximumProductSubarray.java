public class Solution {
    public int maxProduct(int[] A) {
        int n = A.length;
        if (n == 0)
            return 0;
        if (n == 1)
            return A[0];
        int max_product = 1;
        int min_product = 1;
        int result = 0;
        for (int i = 0; i < n; i++) {
            int old_max_product = Math.max(1, max_product);
            if (A[i] > 0) {
                max_product = A[i] * old_max_product;
                min_product *= A[i];
            } else {
                max_product = A[i] * min_product;
                min_product = A[i] * old_max_product;
            }
            result = Math.max(result, max_product);
        }
        return result;
    }
}
