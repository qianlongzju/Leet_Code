#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
using namespace std;
class Solution {
    public:
        string fractionToDecimal(int numerator2, int denominator2) {
            long long numerator = numerator2;
            long long denominator = denominator2;
            string result = "";
            if (numerator * denominator < 0)
                result = "-";
            numerator = abs(numerator);
            denominator = abs(denominator);
            if (numerator % denominator == 0)
                return result + std::to_string(numerator / denominator);
            result += std::to_string(numerator / denominator) + ".";
            numerator %= denominator;
            vector<int> reminders;
            vector<int> numerators;
            numerators.push_back(numerator);
            numerator *= 10;
            while (numerator) {
                reminders.push_back(numerator / denominator);
                numerator %= denominator;
                vector<int>::iterator i = std::find(numerators.begin(), numerators.end(), numerator);
                if (i != numerators.end()) {
                    int left = i - numerators.begin();
                    for (int t=0; t < left; t++)
                        result += std::to_string(reminders[t]);
                    result += "(";
                    for (; left < reminders.size(); left++)
                        result += std::to_string(reminders[left]);
                    result += ")";
                    return result;
                }
                numerators.push_back(numerator);
                numerator *= 10;
            }
            for (vector<int>::iterator index = reminders.begin(); index != reminders.end(); index++) {
                result += std::to_string(*index);
            }
            return result;
        }
};

int main() {
    Solution s = Solution();
    cout << s.fractionToDecimal(1, 6) << endl;
    cout << s.fractionToDecimal(-1, -2147483648) << endl;
    return 0;
}
