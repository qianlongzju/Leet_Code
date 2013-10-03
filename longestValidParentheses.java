import java.util.*;
public class Solution {
    public int longestValidParentheses(String s) {
        // Start typing your Java solution below
        // DO NOT write main() function
        Stack<Integer> stk = new Stack<Integer>();
        char[] ss = new char[s.length()];
        for (int i = 0; i < s.length(); ++i) {
            ss[i] = '#';
        }
        for (int i = 0; i < s.length(); ++i) {
            if (s.charAt(i) == '(') {
                stk.push(i);
            } else if (!stk.empty()) {
                ss[stk.pop()] = '*';
                ss[i] = '*';
            }
        }
        int maxLen = 0, len = 0;
        for (int i = 0; i < s.length(); ++i) {
            if (ss[i] == '*') {
                len ++;
            } else {
                if (len > maxLen) 
                    maxLen = len;
                len = 0;
            }
        }
        if (len > maxLen) {
            maxLen = len;
        }
        return maxLen;
    }
}
