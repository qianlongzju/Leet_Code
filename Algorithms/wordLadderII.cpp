class Solution {
public:
    vector< vector<string> > findLadders(string start, string end, unordered_set<string> &dict) {
        vector<vector<string> > result;
        queue<string> q;
        q.push(start);
        unordered_set<string> visited;
        visited.insert(start);
        unordered_map<string, vector<string> > m;
        unordered_map<string, int> level;
        level[start] = 1;
        int maxLevel = -1;
        while (!q.empty()) {
            string tmp = q.front();
            q.pop();
            if (maxLevel != -1 && level[tmp] > maxLevel) {
                break;
            }
            for (int i=0; i < tmp.size(); i++) {
                for (char c='a'; c <= 'z'; c++) {
                    if (c == tmp[i]) continue;
                    string temp = tmp;
                    temp[i] = c;
                    if (temp == end) {
                        maxLevel = level[tmp];
                        if (m.find(end) == m.end()) {
                            m[end] = vector<string>();
                        }
                        m[end].push_back(tmp);
                    } else if (dict.find(temp) != dict.end()) {
                        if (visited.find(temp) == visited.end()) {
                            q.push(temp);
                            visited.insert(temp);
                            m[temp] = vector<string>();
                            m[temp].push_back(tmp);
                            level[temp] = level[tmp] + 1;
                        } else if (level[tmp]+1 == level[temp]) {
                            m[temp].push_back(tmp);
                        }
                    }
                }
            }
        }
        vector<string> path;
        buildPaths(start, end, m, path, result);
        return result;
    }
    void buildPaths(string &start, string &end, unordered_map<string, vector<string> > &m, 
            vector<string> &path, vector< vector<string> > &result) {
        if (end == start) {
            vector<string> clone(path);
            clone.insert(clone.begin(), start);
            result.push_back(clone);
            return;
        }
        path.insert(path.begin(), end);
        for (int i=0; i < m[end].size(); ++i) {
            buildPaths(start, m[end][i], m, path, result);
        }
        path.erase(path.begin());
    }
};
