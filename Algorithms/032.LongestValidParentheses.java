public class Solution {
    public int longestValidParentheses(String s) {
        Stack<Integer> stk = new Stack<>();
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
                maxLen = Math.max(maxLen, len);
                len = 0;
            }
        }
        return Math.max(maxLen, len);
    }
}
