class Solution {
public:
    int reverse(int x) {
        int y = 0;
        while (x) {
            if (abs(y) > 214748364 || (abs(y) == 214748364 && (x % 10) >= 8)) {
                return 0;
            }
            y = (10 * y) + (x % 10);
            x /= 10;
        }
        return y;
    }
};

