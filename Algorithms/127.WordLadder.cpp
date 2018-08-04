// https://zxi.mytechroad.com/blog/searching/127-word-ladder/
class Solution {
public:
    /*
    int ladderLength(string beginWord, string endWord, vector<string>& wordList) {
        unordered_set<string> dict(wordList.begin(), wordList.end());        
        if (!dict.count(endWord)) return 0;
        queue<string> q;
        q.push(beginWord);
        unordered_set<string> visited;
        visited.insert(beginWord);
        int l = beginWord.length();
        int step = 0;
        while (!q.empty()) {
            step ++;
            for (int size=q.size(); size > 0; size--) {
                string tmp = q.front();
                q.pop();
                for (int i=0; i < l; i++) {
                    char ch = tmp[i];
                    for (char c='a'; c <= 'z'; c++) {
                        if (c == tmp[i]) 
                            continue;
                        tmp[i] = c;
                        if (tmp == endWord) {
                            return step + 1;
                        }
                        if (!dict.count(tmp)) 
                            continue;
                        dict.erase(tmp);
                        q.push(tmp);
                    }
                    tmp[i] = ch;
                }
            }
        }
        return 0;
    }
    */
    int ladderLength(string beginWord, string endWord, vector<string>& wordList) {
        unordered_set<string> dict(wordList.begin(), wordList.end());
        if (!dict.count(endWord)) return 0;

        int l = beginWord.length();

        unordered_set<string> q1{beginWord};
        unordered_set<string> q2{endWord};

        int step = 0;

        while (!q1.empty() && !q2.empty()) {
            ++step;

            // Always expend the smaller queue first
            if (q1.size() > q2.size())
                std::swap(q1, q2);

            unordered_set<string> q;

            for (string w : q1) {
                for (int i = 0; i < l; i++) {
                    char ch = w[i];
                    for (int j = 'a'; j <= 'z'; j++) {
                        if (j == ch) 
                            continue;
                        w[i] = j;
                        if (q2.count(w)) return step + 1;
                        if (!dict.count(w)) continue;
                        dict.erase(w);
                        q.insert(w);
                    }
                    w[i] = ch;
                }
            }

            std::swap(q, q1);
        }
        return 0;
    }
};
