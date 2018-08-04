class Solution {
public:
    vector<vector<string>> findLadders(string beginWord, string endWord, vector<string>& wordList) {
        unordered_set<string> dict(wordList.begin(), wordList.end());
        if (!dict.count(endWord)) return {};

        dict.erase(endWord);

        queue<string> q;
        q.push(beginWord);
        unordered_map<string, vector<string>> parents;
        unordered_map<string, int> levels;
        levels[beginWord] = 1;
        int level = 0;
        bool found = false;
        while (!q.empty() && !found) {
            level ++;
            for (int size = q.size(); size > 0; size--) {
                string tmp = q.front();
                q.pop();
                for (int i=0; i < tmp.size(); i++) {
                    string temp = tmp;
                    for (char c='a'; c <= 'z'; c++) {
                        if (c == tmp[i])
                            continue;
                        temp[i] = c;
                        if (temp == endWord) {
                            parents[temp].push_back(tmp);
                            found = true;
                        } else if (levels.count(temp) && level < levels.at(temp)) {
                            parents[temp].push_back(tmp);
                        }
                        if (!dict.count(temp))
                            continue;
                        dict.erase(temp);
                        q.push(temp);
                        levels[temp] = levels.at(tmp) + 1;
                        parents[temp].push_back(tmp);
                    }
                }
            }
        }
        vector<vector<string>> result;
        if (found) {
            vector<string> path{endWord};
            buildPaths(endWord, beginWord, parents, path, result);
        }
        return result;
    }
    void buildPaths(const string& word, const string& beginWord,
            const unordered_map<string, vector<string>>& parents,
            vector<string>& path, vector<vector<string>>& result) {
        if (word == beginWord) {
            result.push_back(vector<string>(path.rbegin(), path.rend()));
            return;
        }
        for (const string& p: parents.at(word)) {
            path.push_back(p);
            buildPaths(p, beginWord, parents, path, result);
            path.pop_back();
        }
    }
};
