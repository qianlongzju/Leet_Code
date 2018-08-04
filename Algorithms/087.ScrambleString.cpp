class Solution {
public:
    bool isScramble(string s1, string s2) {
        int l1 = s1.length();
        int l2 = s2.length();
        if (l1 != l2)
            return false;
        if (l1 == 0)
            return true;
        if (l1 == 1) 
            return s1 == s2;
        string s11 = s1;
        string s22 = s2;
        sort(s11.begin(), s11.end());
        sort(s22.begin(), s22.end());
        if (s11 != s22)
            return false;
        for (int i=1; i < l1; i++) {
            string s11 = s1.substr(0, i);
            string s12 = s1.substr(i);
            string s21 = s2.substr(0, i);
            string s22 = s2.substr(i);
            if (isScramble(s11, s21) && isScramble(s12, s22))
                return true;
            string s23 = s2.substr(0, l1-i);
            string s24 = s2.substr(l1-i);
            if (isScramble(s11, s24) && isScramble(s12, s23))
                return true;
        }
        return false;
    }
};
