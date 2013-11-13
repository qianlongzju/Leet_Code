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
    bool isInterleave(string s1, string s2, string s3) {
        // Start typing your C/C++ solution below
        // DO NOT write int main() function    
        int n = s1.size();
        int m = s2.size();
        bool IL[n+1][m+1];
        memset(IL, false, sizeof(IL));
        if ((m+n) != s3.size())
            return false;
        for (int i=0; i <= n; ++i) {
            for (int j=0; j <= m; ++j) {
                if (i == 0 && j == 0)
                    IL[i][j] = true;
                else if (i == 0) {
                   if (s2[j-1] == s3[j-1])
                       IL[i][j] = IL[i][j-1];
                }
                else if (j == 0) {
                   if (s1[i-1] == s3[i-1])
                       IL[i][j] = IL[i-1][j];
                }
                else if (s1[i-1] == s3[i+j-1] && s2[j-1] != s3[i+j-1]) 
                    IL[i][j] = IL[i-1][j];
                else if (s2[j-1] == s3[i+j-1] && s1[i-1] != s3[i+j-1])
                    IL[i][j] = IL[i][j-1];
                else if (s1[i-1] == s3[i+j-1] && s2[j-1] == s3[i+j-1]) 
                    IL[i][j] = IL[i][j-1] || IL[i-1][j];
            }
        }
        return IL[n][m];
    }
};
int main() {
    Solution s;
    string s1 = "aabcc";
    string s2 = "dbbca";
    string s3 = "aadbbcbcac";
    cout << s.isInterleave(s1, s2, s3) << endl;
    s3 = "aadbbbaccc";
    cout << s.isInterleave(s1, s2, s3) << endl;
    return 0;
}
