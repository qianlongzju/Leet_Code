import java.util.*;
public class Solution {
    public int numDecodings(String s) {
        HashMap<Integer, Integer> m = new HashMap<Integer, Integer>();
        if (s.length() == 0)
            return 0;
        return numDecodings(s, 0, m);
    }
    private int numDecodings(String s, int index, HashMap<Integer, Integer> m) {
        if (m.get(index) != null) {
            return m.get(index);
        }
        int n = s.length();
        if (index == n) {
            return 1;
        } else if (index == n-1) {
            if (s.charAt(index) == '0') {
                return 0;
            } else {
                return 1;
            }
        } else {
            int count = 0;
            if (s.charAt(index) != '0') {
                count += numDecodings(s, index+1, m);
                if ((s.charAt(index) == '1') ||  
                        (s.charAt(index) == '2' && s.charAt(index+1)-'0' <= 6)) {
                    count += numDecodings(s, index+2, m);
                }
            }
            m.put(index, count);
            return count;
        }
    }
}
