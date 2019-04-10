class Solution {
public:
    string minWindow(string S, string T) {
        int needToFind[256] = {0};
        int hasFound[256] = {0};
        for (int i=0; i < 256; ++i) {
            needToFind[i] = 0;
            hasFound[i] = 0;
        }
        for (int i=0; i < T.size(); ++i) {
            needToFind[T[i]] ++;
        }
        int count = 0;
        int begin = 0;
        int end = 0;
        int minLength = INT_MAX;
        int startIndex = 0;
        while (end < S.size()) {
            if (needToFind[S[end]] == 0) {
                end ++;
                continue;
            }
            hasFound[S[end]] ++;
            if (hasFound[S[end]] <= needToFind[S[end]]) {
                count ++;
            }
            if (count == T.size()) {
                while (needToFind[S[begin]] == 0 || hasFound[S[begin]] > needToFind[S[begin]]) {
                    if (hasFound[S[begin]] > needToFind[S[begin]]) {
                        hasFound[S[begin]] --;
                    }
                    begin ++;
                }
                int length = end - begin + 1;
                if (length < minLength) {
                    minLength = length;
                    startIndex = begin;
                }
            }
            end ++;
        }
        if (count == T.size()) {
            return S.substr(startIndex, minLength);
        } else {
            return "";
        }
    }
};
