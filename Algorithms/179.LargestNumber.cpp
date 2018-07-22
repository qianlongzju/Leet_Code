class Solution {
    public:
        string largestNumber(vector<int>& nums) {
            sort(nums.begin(), nums.end(), cmp);
            if (nums[0] == 0)
                return "0";
            string result = "";
            for (int i = 0; i < nums.size(); i++) {
                result += to_string(nums[i]);
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
