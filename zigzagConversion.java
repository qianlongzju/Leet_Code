public class Solution {
    public String convert(String s, int nRows) {
        // Start typing your Java solution below
        // DO NOT write main() function
        if (nRows == 1) {
            return s;
        }
        String result = "";
        int offset = 2*(nRows-1);
        for (int i=0; i < nRows; i++) {
            if (i == 0 || i == nRows-1) {
                for (int j=0; i+j*offset < s.length(); j++) {
                    result += s.charAt(i+offset*j);
                }
            }
            else {
                boolean odd = false;
                for (int j=0; ; j++) {
                    if (odd) {
                        if (i+(offset)*(j+1)/2-2*i >= s.length()) {
                            break;
                        }
                        result += s.charAt(i+(offset)*(j+1)/2-2*i);
                    }
                    else {
                        if (i+offset*(j/2) >= s.length()) {
                            break;
                        }
                        result += s.charAt(i+offset*(j/2));
                    }
                    odd = !odd;
                }
            }
        }
        return result;
    }
}
