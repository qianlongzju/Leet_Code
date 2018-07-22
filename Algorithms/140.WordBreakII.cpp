class Solution {
public:
    vector<string> wordBreak(string s, vector<string>& wordDict) {
        // 长度为 n 的字符串有 n+1 个隔板
        vector<bool> f(s.length() + 1, false);
        // path[i][j] 为 true,表示 s[j, i) 是一个合法单词,可以从 j 处切开
        // 第一行未用
        vector<vector<bool>> prev(s.length()+1, vector<bool>(s.length()));
        f[0] = true;
        for (int i = 1; i <= s.length(); ++i) {
            for (int j = i - 1; j >= 0; --j) {
                if (f[j] && std::find(wordDict.beign(), wordDict.end(), s.substr(j, i - j)) != wordDict.end()) {
                    f[i] = true;
                    prev[i][j] = true;
                }
            }
        }
        vector<string> result;
        vector<string> path;
        gen_path(s, prev, s.length(), path, result);
        return result;
    }
private:
    // DFS 遍历树,生成路径
    void gen_path(const string& s, const vector<vector<bool>>& prev,
            int cur, vector<string>& path, vector<string>& result) {
        if (cur == 0) {
            string tmp;
            for (auto iter = path.rbegin(); iter != path.rend(); ++iter)
                tmp += *iter + " ";
            tmp.erase(tmp.end()-1);
            result.push_back(tmp);
        }
        for (int i = 0; i < cur; ++i) {
            if (prev[cur][i]) {
                path.push_back(s.substr(i, cur - i));
                gen_path(s, prev, i, path, result);
                path.pop_back();
            }
        }
    }
    /*
    vector<string> wordBreak(string s, vector<string>& wordDict) {
        vector<string> r;
        int n = s.size();
        if (n == 0 || wordDict.size() == 0)
            return r;
        vector<bool> wb(n, false);
        vector<vector<bool>> prev(n, vector<bool>(n, false));
        for (int i=0; i < n; ++i) {
            if (wb[i] == false && std::find(wordDict.begin(), wordDict.end(), s.substr(0, i+1)) != wordDict.end()) {
                wb[i] = true;
                prev[0][i] = true;
            }
            if (wb[i] == true) {
                for (int j=i+1; j < n; ++j) {
                    if (std::find(wordDict.begin(), wordDict.end(), s.substr(i+1, (j+1)-(i+1))) != wordDict.end()) {
                        wb[j] = true;
                        prev[i][j] = true;
                    }
                }
            }
        }
        vector<string> path;
        set<string> result;
        buildPaths(0, s, prev, path, result, wb);
        for (set<string>::iterator it=result.begin(); it!=result.end(); ++it) {
            r.push_back(*it);
        }
        return r;
    }
    void buildPaths(int cur, string& s, vector<vector<bool>>& prev,
            vector<string>& path, set<string>& result, vector<bool>& wb) {
        if (cur == (s.size()-1)) {
            if (path.size() != 0) { 
                string p;
                for (int i=0; i < path.size(); ++i) {
                    p += path[i] + " ";
                }
                p.erase(p.end()-1);
                result.insert(p);
            } else {
                if (wb[cur])
                    result.insert(s.substr(0, cur+1));
            }
            return;
        }
        for (int i=cur+1; i < s.size(); ++i) {
            if (prev[cur][i]) {
                path.push_back(s.substr(cur+1, i-cur));
                buildPaths(i, s, prev, path, result, wb);
                path.pop_back();
            }
        }
    }
    */
};
