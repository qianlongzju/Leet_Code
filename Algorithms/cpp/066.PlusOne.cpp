class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        int p = 1;
        for (int i=digits.size()-1; i >= 0; i--) {
            digits[i] += p;
            p = digits[i] / 10;
            digits[i] %= 10;
            if (p == 0)
                return digits;
        }
        if (p != 0) {
            digits.insert(digits.begin(), 1);
        }
        return digits;
    }
};
