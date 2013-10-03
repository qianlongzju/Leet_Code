import java.util.*;
public class Solution {
    public int atoi(String str) {
        // Start typing your Java solution below
        // DO NOT write main() function
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
                result = 10*result + (str.charAt(i) - '0');
            } else {
                break;
            }
            i ++;
        }
        if (positive && result > 2147483647L) 
            return 2147483647;
        else if (!positive && result > 2147483648L)
            return -2147483648;
        if (positive)
            return (int)result;
        else 
            return -(int)result;
    }
}

