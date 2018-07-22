class Solution {
public:
    int ladderLength(string start, string end, unordered_set<string> &dict) {
        if (start == end) {
            return 2;
        }
        queue<string> q;
        q.push(start);
        unordered_set<string> visited;
        visited.insert(start);
        map<string, string> m;
        while (!q.empty()) {
            string tmp = q.front();
            q.pop();
            for (int i=0; i < tmp.size(); i++) {
                for (char c='a'; c <= 'z'; c++) {
                    if (c == tmp[i]) continue;
                    string temp = tmp;
                    temp[i] = c;
                    if (temp == end) {
                        int length = 2;
                        while (tmp != start) {
                            tmp = m[tmp];
                            length++;
                        }
                        return length;
                    }
                    
                    if (dict.find(temp) != dict.end() && 
                            visited.find(temp) == visited.end()) {
                        q.push(temp);
                        visited.insert(temp);
                        m[temp] = tmp;
                    }
                }
            }
        }
        return 0;
    }
};
