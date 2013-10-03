#include <iostream>
using namespace std;
class Solution {
public:
    string convert(string s, int nRows) {
        // Start typing your C/C++ solution below
        // DO NOT write int main() function    
        if (nRows == 1) {
            return s;
        }
        string result = "";
        int offset = 2*(nRows-1);
        for (int i=0; i < nRows; i++) {
            if (i == 0 || i == nRows-1) {
                for (int j=0; i+j*offset < s.size(); j++) {
                    result += s[i+offset*j];
                }
            }
            else {
                bool odd = false;
                for (int j=0; ; j++) {
                    if (odd) {
                        if (i+(offset)*(j+1)/2-2*i >= s.size()) {
                            break;
                        }
                        result += s[i+(offset)*(j+1)/2-2*i];
                    }
                    else {
                        if (i+offset*(j/2) >= s.size()) {
                            break;
                        }
                        result += s[i+offset*(j/2)];
                    }
                    odd = !odd;
                }
            }
        }
        return result;
    }
};
int main() {
    Solution s;
    //string a("PAYPALISHIRING");
    //cout << a << endl;
    //cout << s.convert(a, 3) << endl;
    //cout << "PAHNAPLSIIGYIR" << endl;
    //string b("ABCD");
    //cout << s.convert(b, 3) << endl;
    string c = "PAYPALISHIRING";
    cout << s.convert(c, 4) << endl;
    cout << "PINALSIGYAHRPI" << endl;

    return 0;
}
