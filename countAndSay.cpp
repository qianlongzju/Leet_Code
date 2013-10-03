#include <string>
#include <vector>
#include <iostream>
using namespace std;
class Solution {
public:
    string countAndSay(int n) {
        // Start typing your C/C++ solution below
        // DO NOT write int main() function
        std::vector<int> v;
        std::vector<int> w;
        string result;
        v.push_back(1);
        while (--n) {
            int count = 1;
            for (int i=1; i < v.size(); ++i)
            {
                if (v[i] == v[i-1]) {
                    count ++;
                }
                else {
                    w.push_back(count);
                    w.push_back(v[i-1]);
                    count = 1;
                }
            }
            w.push_back(count);
            w.push_back(v[v.size()-1]);
            v = w;
            w.clear();
        }
        for (int i = 0; i < v.size(); ++i)
        {
            result += v[i] + '0';
        }
        return result;
    }
};

int main() {
    Solution s;
    cout << s.countAndSay(3) << endl;
    cout << s.countAndSay(4) << endl;
    cout << s.countAndSay(5) << endl;
    return 0;
}

