#include "leetcode.h"
class Solution {
public:
    bool isValid(string s) {
        // Start typing your C/C++ solution below
        // DO NOT write int main() function
        vector<char> v;
        for (int i=0; i < s.size(); i++) {
            if (s[i] == '(' || s[i] == '{' || s[i] == '[') {
                v.push_back(s[i]);
            }
            else {
                if (v.empty()) {
                    return false;
                }
                char c = v.back();
                v.pop_back();
                if (c == '(' && s[i] == ')') {
                    continue;
                }
                if (c == '{' && s[i] == '}') {
                    continue;
                }
                if (c == '[' && s[i] == ']') {
                    continue;
                }
                return false;
            }
        }
        if (v.empty()) {
            return true;
        }
        else {
            return false;
        }
    }
};
