class Solution {
public:
    int numDecodings(string s) {
        map<int, int> m;
        if (s.size() == 0)
            return 0;
        return numDecodings(s, 0, m);
    }
    int numDecodings(string s, int index, map<int, int> &m) {
        if (m.find(index) != m.end()) {
            return m[index];
        }
        int n = s.size();
        if (index == n) {
            return 1;
        } else if (index == n-1) {
            if (s[index] == '0') {
                return 0;
            } else {
                return 1;
            }
        } else {
            int count = 0;
            if (s[index] != '0') {
                count += numDecodings(s, index+1, m);
                if ((s[index] == '1') ||  
                        (s[index] == '2' && s[index+1]-'0' <= 6)) {
                    count += numDecodings(s, index+2, m);
                }
            }
            m[index] = count;
            return count;
        }
    }
};
