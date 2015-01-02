public class Solution {
    public int trailingZeroes(int n) {
        int a = n/5;
        int count = a;
        while (a > 0) {
        	count += a/5;
        	a /= 5;
        }
        return count;
    }
}