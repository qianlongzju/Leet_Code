#include "leetcode.h"
#include <cstring>
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
    vector<string> wordBreak(string s, unordered_set<string> &dict) {
        // Note: The Solution object is instantiated only once and is reused by each test case.
        set<string> result;
        int n = s.size();
        int wb[n];
        memset(wb, -1, sizeof(wb));
        for (int i=0; i < n; ++i) {
            if (dict.find(s.substr(0, i+1)) != dict.end()) {
                wb[i] = -2;
            }
            if (wb[i] != -1) {
                if (i == n-1) {
                    //for (int i=0; i < n; ++i) {
                    //    cout << wb[i] << " ";
                    //}
                    //cout << endl;
                    string temp = "";
                    int k = i;
                    while (wb[k] != -2) {
                        //cout << "k:" << k << ",wb[k]" << wb[k] << endl;
                        temp = s.substr(wb[k]+1, k-wb[k]) + " " + temp;
                        k = wb[k];
                    }
                    temp = s.substr(0, k+1) + " " + temp;
                    result.insert(temp.substr(0, temp.size()-1));
                }
                int l = i;
                for (int j=l+1; j < n; ++j) {
                    if (dict.find(s.substr(l+1, (j+1)-(l+1))) != dict.end()) {
                        //cout << "l:" << l << endl;
                        //cout << "j:" << j << endl;
                        wb[j] = l;
                        l = j;
                    }
                    if (j == n-1 && wb[j] != -1) {
                        string temp = "";
                        int k = j;
                        while (wb[k] != -2) {
                            //cout << "k:" << k << ",wb[k]" << wb[k] << endl;
                            temp = s.substr(wb[k]+1, k-wb[k]) + " " + temp;
                            k = wb[k];
                        }
                        temp = s.substr(0, k+1) + " " + temp;
                        result.insert(temp.substr(0, temp.size()-1));
                    }
                }
            }
        }
        vector<string> r;
        for (set<string>::iterator it=result.begin(); it != result.end(); it++) {
            r.push_back(*it);
        }
        return r;
    }
};
int main() {
    Solution s;
    unordered_set<string> dict;
    dict.insert("cat");
    dict.insert("cats");
    dict.insert("and");
    dict.insert("sand");
    dict.insert("dog");
    vector<string> result = s.wordBreak("catsanddog", dict);
    for (int i=0; i < result.size(); ++i) {
        cout << result[i] << endl;
    }
    dict.clear();
    dict.insert("a");
    dict.insert("b");
    result = s.wordBreak("ab", dict);
    for (int i=0; i < result.size(); ++i) {
        cout << result[i] << endl;
    }
    dict.clear();
    dict.insert("aaaa");
    dict.insert("aaa");
    result = s.wordBreak("aaaaaaa", dict);
    for (int i=0; i < result.size(); ++i) {
        cout << result[i] << endl;
    }
    return 0;
}

