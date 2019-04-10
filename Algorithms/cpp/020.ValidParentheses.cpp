class Solution {
public:
    bool isValid(string s) {
        unordered_map<char, char> m;
        m['('] = ')';
        m['['] = ']';
        m['{'] = '}';
        vector<char> v;
        for (int i=0; i < s.size(); i++) {
            if (m.find(s[i]) != m.end()) {
                v.push_back(s[i]);
            }
            else {
                if (v.empty()) return false;
                char c = v.back();
                v.pop_back();
                if (m[c] != s[i]) return false;
            }
        }
        return v.empty();
    }
};
