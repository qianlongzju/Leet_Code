class Solution {
public:
    bool isMatch(string s, string p) {
        bool star = false;
        int i;
        for (i=0; i != s.size(); i++) {
            switch (p[i]) {
                case '?':
                    break;
                case '*':
                    star = true;
                    p = p.substr(i+1);
                    s = s.substr(i);
                    i = -1;
                    while (p.size() > 0 and p[0] == '*') {
                        p = p.substr(1);
                    }
                    if (p.size() == 0) {
                        return true;
                    }
                    break;
                default:
                    if (s[i] != p[i]) {
                        if (star) {
                            s = s.substr(1);
                            i = -1;
                        } else {
                            return false;
                        }
                    }
                    break;
            }
        }
        while (i < p.size() && p[i] == '*') {
            i ++;
        }
        return i == p.size();
    }
};
