#include "leetcode.h"
class Solution {
public:
    int evalRPN(vector<string> &tokens) {
        stack<int> stk;
        for (int i=0; i < tokens.size(); ++i) {
            if (tokens[i] == "+") {
                int a = stk.top();
                stk.pop();
                int b = stk.top();
                stk.pop();
                stk.push(b + a);
            } else if (tokens[i] == "-") {
                int a = stk.top();
                stk.pop();
                int b = stk.top();
                stk.pop();
                stk.push(b - a);
            } else if (tokens[i] == "*") {
                int a = stk.top();
                stk.pop();
                int b = stk.top();
                stk.pop();
                stk.push(b * a);
            } else if (tokens[i] == "/") {
                int a = stk.top();
                stk.pop();
                int b = stk.top();
                stk.pop();
                stk.push(b / a);
            } else {
                stk.push(atoi(tokens[i].c_str()));
            }
        }
        return stk.top();
    }
};
int main() {
    Solution s;
    vector<string> tokens;
    tokens.push_back("2");
    tokens.push_back("1");
    tokens.push_back("+");
    tokens.push_back("3");
    tokens.push_back("*");
    cout << s.evalRPN(tokens) << endl;
    tokens.clear();
    tokens.push_back("4");
    tokens.push_back("13");
    tokens.push_back("5");
    tokens.push_back("/");
    tokens.push_back("+");
    cout << s.evalRPN(tokens) << endl;
    return 0;
}

