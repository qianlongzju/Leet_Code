import java.util.*;
public class Solution {
    public int atoi(String str) {
        int len = str.length();
        int i = 0;
        boolean positive = true;
        long result = 0;
        while (i < len && Character.isWhitespace(str.charAt(i))) 
            i ++;
        if (i < len && str.charAt(i) == '+') 
            i ++;
        else if (i < len && str.charAt(i) == '-') {
            positive = false;
            i ++;
        }
        while (i < len) {
            if (Character.isDigit(str.charAt(i))) {
                if (result > 214748364 || (result == 214748364 && (str.charAt(i) - '0') >= 8)) {
                    return positive? 2147483647:-2147483648;
                }
                result = 10*result + (str.charAt(i) - '0');
            } else {
                break;
            }
            i ++;
        }
        if (positive)
            return (int)result;
        else 
            return -(int)result;
    }
}
