import java.util.*;
public class Solution {
    public boolean isMatch(String s, String p) {
        // Start typing your Java solution below
        // DO NOT write main() function
        int n = s.length();
        int m = p.length();
        if (m == 0)
            return n == 0;
        if (m == 1) {
            if (n != 1)
                return false;
            return ((p.charAt(0) == s.charAt(0)) || (p.charAt(0) == '.'));
        }
        // next char is not '*': must match current character
        if (p.charAt(1) != '*') {
            if (n == 0) 
                return false;
            return ((p.charAt(0) == s.charAt(0)) || (p.charAt(0) == '.')) && 
                isMatch(s.substring(1), p.substring(1));
        }
        // next char is '*'
        while (n > 0 && (p.charAt(0) == s.charAt(0)) || (p.charAt(0) == '.' && n != 0)) {
            if (isMatch(s, p.substring(2))) 
                return true;
            s = s.substring(1);
            n = s.length();
        }
        return isMatch(s, p.substring(2));
    }
}
