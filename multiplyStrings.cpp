class Solution {
public:
    string multiply(string num1, string num2) {
        // Start typing your C/C++ solution below
        // DO NOT write int main() function
        int m = num1.size();
        int n = num2.size();
        int result[m+n];
        for (int i=0; i < m+n; i++) {
            result[i]= 0;
        }
        int p, i, j;
        for (i=0; i < m; i++) {
            p = 0;
            for (j=0; j < n; j++) {
                int q = result[i+j] + (num1[m-1-i]-'0') * (num2[n-1-j]-'0') + p;
                result[i+j] = q % 10;
                p = q / 10;
            }
            if (p != 0) {
                result[i+j] = p;
            }
        }
        if (p != 0) {
            result[m+n-1] = p;
        }
        string s;
        int k = m+n-1;
        for (i=k; i >= 0 && result[i] == 0; i--) {
            ;
        }
        k = i;
        for (int i=k; i >= 0; i--) {
            s += result[i] + '0';
        }
        if (s.size() == 0) {
            s += '0';
        }
        return s;
    }
};
