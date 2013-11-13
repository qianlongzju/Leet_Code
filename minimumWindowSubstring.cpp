#include "leetcode.h"
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<string> vs;
typedef pair<int, int> ii;
typedef vector<ii> vii;
typedef vector< pair<double,ii> > vdii;
#define sz(a) int((a).size())
#define pb push_back
#define all(c) (c).begin(),(c).end()
#define tr(c,i) for(typeof((c).begin()) i = (c).begin(); i != (c).end(); i++)
#define present(c,x) ((c).find(x) != (c).end())
#define cpresent(c,x) (find(all(c),x) != (c).end())
using namespace std;
class Solution {
public:
    string minWindow(string S, string T) {
        // Note: The Solution object is instantiated only once and is reused by each test case.
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
int main() {
    Solution s;
    string S = "ADOBECODEBANC";
    string T = "ABC";
    cout << s.minWindow(S, T) << endl;
    cout << "right answer: BANC" << endl;
    cout << s.minWindow("a", "aa") << endl;
    cout << "right answer: " << endl;
    return 0;
}
