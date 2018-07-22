class Solution {
public:
    vector<string> generateParenthesis(int n) {
        vector<string> result;
        string s;
        generateParenthesis(n, 0, 0, s, result);
        return result;
    }
    void generateParenthesis(int n, int left, int right, string s,
            vector<string>& result) {
        if (left == n && right == n) {
            result.push_back(s);
            return;
        }
        if (left < n) {
            generateParenthesis(n, left+1, right, s + "(", result);
        }
        if (right < left) {
            generateParenthesis(n, left, right+1, s + ")", result);
        }
    }
};
