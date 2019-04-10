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
                return result + to_string(numerator / denominator);
            result += to_string(numerator / denominator) + ".";
            numerator %= denominator;
            vector<int> reminders;
            vector<int> numerators;
            numerators.push_back(numerator);
            numerator *= 10;
            while (numerator) {
                reminders.push_back(numerator / denominator);
                numerator %= denominator;
                vector<int>::iterator i = find(numerators.begin(), numerators.end(), numerator);
                if (i != numerators.end()) {
                    int left = i - numerators.begin();
                    for (int t=0; t < left; t++)
                        result += to_string(reminders[t]);
                    result += "(";
                    for (; left < reminders.size(); left++)
                        result += to_string(reminders[left]);
                    result += ")";
                    return result;
                }
                numerators.push_back(numerator);
                numerator *= 10;
            }
            for (vector<int>::iterator index = reminders.begin(); index != reminders.end(); index++) {
                result += to_string(*index);
            }
            return result;
        }
};
