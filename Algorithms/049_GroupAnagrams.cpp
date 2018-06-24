class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        vector<vector<string>> result;
        map<string, vector<string> > m;
        string temp;
        for (int i=0; i < strs.size(); ++i) {
            temp = strs[i];
            sort(temp.begin(), temp.end());
            if (m.find(temp) == m.end()) {
                vector<string> a;
                a.push_back(strs[i]);
                m[temp] = a;
            } else {
                m[temp].push_back(strs[i]);
            }
        }
        for (map<string, vector<string> >::iterator it=m.begin(); it != m.end(); it++) {
            result.push_back(it->second);
        }
        return result;
    }
};
