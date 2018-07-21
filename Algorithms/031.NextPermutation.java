public class Solution {
    public void nextPermutation(int[] num) {
        for (int i=num.length-1; i > 0; i--) {
            if (num[i] <= num[i-1]) {
                continue;
            }
            for (int j=num.length-1; j >= i; j--) {
                if (num[j] > num[i-1]) {
                    int temp = num[i-1];
                    num[i-1] = num[j];
                    num[j] = temp;
                    for(int p=i, q=num.length-1; p < q; p++, q--) {
                        temp = num[p];
                        num[p] = num[q];
                        num[q] = temp;
                    }
                    return;
                }
            }
        }
        for(int p=0, q=num.length-1; p < q; p++, q--) {
            int temp = num[p];
            num[p] = num[q];
            num[q] = temp;
        }
    }
}