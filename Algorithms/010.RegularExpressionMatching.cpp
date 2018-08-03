//  If the next character of p is NOT '*', then it must match the current character of s. Continue pattern matching with the next character of both s and p.
//  If the next character of p is '*', then we do a brute force exhaustive matching of 0, 1, or more repeats of current character of p… Until we could not match any more characters.
class Solution {
public:
    bool isMatch(string s, string p) {
        if (p == "")
            return s == "";
        // next char is not '*': must match current character
        if (p[1] != '*') {
            return ((p[0] == s[0]) || (p[0] == '.' && s != "")) && isMatch(s.substr(1), p.substr(1));
        }
        // next char is '*'
        while ((p[0] == s[0]) || (p[0] == '.' && s != "")) {
            if (isMatch(s, p.substr(2))) 
                return true;
            s = s.substr(1);
        }
        return isMatch(s, p.substr(2));
    }
};
