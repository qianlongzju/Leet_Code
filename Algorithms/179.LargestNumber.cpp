class Solution {
    public:
        string largestNumber(vector<int>& num) {
            sort(num.begin(), num.end(), cmp);
            if (num[0] == 0)
                return "0";
            string result = "";
            for (int i = 0; i < num.size(); i++) {
                result += to_string(num[i]);
            }
            return result;
        }
    private:
        bool static cmp(long x, long y) {
            long i = 10;
            while (i <= y) {
                i *= 10;
            }
            long xx = x*i + y;
            i = 10;
            while (i <= x) {
                i *= 10;
            }
            long yy = y * i + x;
            if (xx <= yy)
                return false;
            return true;
        }
};
