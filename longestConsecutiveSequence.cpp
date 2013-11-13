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
    int longestConsecutive(vector<int> &num) {
        // Start typing your C/C++ solution below
        // DO NOT write int main() function
        unordered_set<int> m;
        for (int i=0; i < num.size(); ++i) {
            m.insert(num[i]);
        }
        int longestLength = 0;
        for (int i=0; i < num.size(); ++i) {
            int j = num[i];
            int length = 1;
            while (m.find(j+1) != m.end()) {
                m.erase(j+1);
                j ++;
                length ++;
            }
            j = num[i];
            while (m.find(j-1) != m.end()) {
                m.erase(j-1);
                j --;
                length ++;
            }
            if (length > longestLength) {
                longestLength = length;
            }
        }
        return longestLength;
    }
};
int main() {
    Solution s;
    vector<int> num;
    num.push_back(100);
    num.push_back(4);
    num.push_back(200);
    num.push_back(1);
    num.push_back(3);
    num.push_back(2);
    cout << s.longestConsecutive(num) << endl;
    return 0;
}

