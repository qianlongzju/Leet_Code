public class Solution {
    public boolean isPalindrome(int x) {
        // Start typing your Java solution below
        // DO NOT write main() function
        if (x < 0) {
            return false;
        }
        long i = 1;
        while (i*10 <= x) {
            i *= 10;
        }
        while (x >= 10) {
            if (x/i == x%10) {
                x = x % (int)i;
                x /= 10;
                i /= 100;
            }
            else {
                return false;
            }
        }
        return true;
    }
}
