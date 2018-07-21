public class Solution {
    public boolean isNumber(String s) {
        int len = s.length();
        int i = len-1;
        while (i >= 0 && Character.isWhitespace(s.charAt(i)))
            i --;
        len = i + 1;
        i = 0;
        while (i < len && Character.isWhitespace(s.charAt(i))) 
            i ++;
        if (i < len && s.charAt(i) == '+') 
            i ++;
        else if (i < len && s.charAt(i) == '-') {
            i ++;
        }
        if (i == len) {
            return false;
        }
        boolean isE = false;
        boolean isPoint = false;
        boolean hasNum = false;
        while (i < len) {
            if (Character.isDigit(s.charAt(i))) {
                hasNum = true;
            } else if (!isE && hasNum && s.charAt(i) == 'e') {
                if (i+1 >= len)
                    return false;
                if (s.charAt(i+1) == '+' || s.charAt(i+1) == '-') {
                    if (i+2 >= len || !Character.isDigit(s.charAt(i+2))) {
                        return false;
                    }
                    i += 2;
                }
                else if (Character.isDigit(s.charAt(i+1))) {
                    i ++ ;
                }
                else 
                    return false;
                isE = true;
            } else if (!isPoint && !isE && s.charAt(i) == '.') {
                if ((i > 0 && Character.isDigit(s.charAt(i-1))) || (i < len-1 && Character.isDigit(s.charAt(i+1))))
                    isPoint = true;
                else
                    return false;
            } else {
                return false;
            }
            i ++;
        }
        return true;
    }
}

