public class Solution {
    private static final String[] symbols = {"M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"};
    private static final int[] values = {1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1};
    public String intToRoman(int nums) {
        StringBuilder sb = new StringBuilder();
        int i = 0;
        while (nums != 0) {
            int k = nums / values[i];
            for (int j = 0; j < k; j++) {
                sb.append(symbols[i]);
                nums -= values[i];
            }
            i++;
        }
        return sb.toString();
    }
}

