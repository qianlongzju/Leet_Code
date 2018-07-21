class Solution {
public:
    string longestPalindrome(string s) {
        int length = s.size();
        bool table[length][length];
        int maxLen = 1;
        int maxIndex = 0;
        for (int i=0; i < length; i++) {       
            for (int j = 0; j < length; ++j)
                table[i][j] = false;
            table[i][i] = true;
            if (i+1 < length && s[i] == s[i+1]) {
                table[i][i+1] = true;
                maxLen = 2;
                maxIndex = i;
            }
        }
        for (int len=3; len <= length; len++) {
            for (int i=0; i < length-len+1; i++) {
                if (s[i] == s[i+len-1] && table[i+1][i+len-2] == true) {
                    table[i][i+len-1] = true;
                    maxLen = len;
                    maxIndex = i;
                }
            }
        }
        return s.substr(maxIndex, maxLen);
    }
};
int main(int argc, char const *argv[])
{
    vector<int> a, b;
    a.push_back(1);
    a.push_back(2);
    b.push_back(2);
    b.push_back(1);
/*  a.push_back(1);
    a.push_back(3);
    a.push_back(2);
    a.push_back(4);
    a.push_back(6);
    a.push_back(5);
    b.push_back(1);
    b.push_back(2);
    b.push_back(3);
    b.push_back(4);
    b.push_back(5);
    b.push_back(6);*/
    Solution s;
    cout << s.longestPalindrome("babc") << endl;
    cout << s.longestPalindrome("aaaa") << endl;
    // while (p != NULL) {
    //  cout << p->val;
    //  p = p->left;
    // }
    //for (int i = 0; i < 3; ++i)
    //{
    //  cout << A[i];
    //}
    //cout << A[0]  << A[1] << A[2] << endl;
    return 0;
}
