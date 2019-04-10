class Solution {
public:
    int longestValidParentheses(string s) {
        stack<int> stk;
        for (int i = 0; i < s.size(); ++i) {
            if (s[i] == '(') {
                stk.push(i);
            } else if (!stk.empty()) {
                s[stk.top()] = '*';
                s[i] = '*';
                stk.pop();
            }
        }
        int maxLen = 0, len = 0;
        for (int i = 0; i < s.size(); ++i) {
            if (s[i] == '*') {
                len ++;
            } else {
                maxLen = max(maxLen, len);
                len = 0;
            }
        }
        return max(maxLen, len);
    }
};
