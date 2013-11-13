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
    int singleNumber(int A[], int n) {
        // Note: The Solution object is instantiated only once and is reused by each test case.
        int result = 0;
        for (int j=0; j < 32; ++j) {
            int tmp = 0;
            for (int i=0; i < n; ++i) {
                if (A[i] & (1<<j)) {
                    tmp ++;
                }
            }
            result += (tmp%3) << j;
        }
        return result;
    }
};
int main() {
    Solution s;
    int A[] = { 3, 3, 3, 4};
    cout << s.singleNumber(A, 4) << endl;
    int B[] = {-2,-2,1,1,-3,1,-3,-3,-4,-2};
    cout << s.singleNumber(B, 10) << endl;
    int C[] = {43,16,45,89,45,-2147483648,45,2147483646,-2147483647,-2147483648,43,2147483647,-2147483646,-2147483648,89,-2147483646,89,-2147483646,-2147483647,2147483646,-2147483647,16,16,2147483646,43};
    cout << s.singleNumber(C, 25) << endl;

    return 0;
}
