public class Solution {
    public int[] plusOne(int[] digits) {
        // Start typing your Java solution below
        // DO NOT write main() function
        int p = 0;
        for (int i=digits.length-1; i >= 0; i--) {
            int q = p + digits[i];
            if (i == digits.length-1) {
                q ++;
            }
            digits[i] = q % 10;
            p = q / 10;
        }
        if (p != 0) {
            int[] new_digits = new int[digits.length+1];
            new_digits[0] = 1;
            for (int i=1; i < new_digits.length; i++){
                new_digits[i] = digits[i-1];
            }
            return new_digits;
        }
        else {
            return digits;
        }
    }
}
