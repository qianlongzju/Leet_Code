class Solution {
public:
    string intToRoman(int num) {
        string symbols[] = {"M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"};
        int values[] = {1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1};
        string s;
        int i = 0;
        while (num != 0) {
            int k = num / values[i];
            for (int j = 0; j < k; j++) {
                s += symbols[i];
                num -= values[i];
            }
            i++;
        }
        return s;
    }
};
int main() {
    Solution s;
    cout << s.intToRoman(1000) << endl;
    return 0;
}

