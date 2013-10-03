public class Solution {
    public int reverse(int x) {
        // Start typing your Java solution below
        // DO NOT write main() function
        boolean positive = true;
        if (x < 0) {
            positive = false;
            x = -x;
        }
        int y = 0;
        while (x != 0) {
            y = (10 * y) + (x % 10);
            x /= 10;
        }
        if (positive)
            return y;
        else
            return -y;
        
    }
}
