class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        if (strs.size() == 0) {
            return "";
        }
        if (strs.size() == 1) {
            return strs[0];
        }
        int i;
        for (i=0; i < strs[0].size(); i++) {
            int j;
            for (j=1; j < strs.size(); j++) {
                if (i < strs[j].size() && strs[j][i] == strs[0][i]) {
                    ;
                }
                else {
                    break;
                }
            }
            if (j != strs.size()) {
                break;
            }
        }
        return strs[0].substr(0, i);
    }
};
