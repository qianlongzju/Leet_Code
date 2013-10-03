class Solution {
public:
    vector<int> plusOne(vector<int> &digits) {
        // Start typing your C/C++ solution below
        // DO NOT write int main() function
        int p = 0;
        for (int i=digits.size()-1; i >= 0; i--) {
            int q = p + digits[i];
            if (i == digits.size()-1) {
                q ++;
            }
            digits[i] = q % 10;
            p = q / 10;
        }
        if (p != 0) {
            digits.insert(digits.begin(), 1);
        }
        return digits;
    }
};
