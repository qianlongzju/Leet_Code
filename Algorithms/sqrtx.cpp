class Solution {
public:
    int mySqrt(int x) {
        if (x == 0)  return 0;
        double last;
        double res = x;
        while (last != res) {
            last = res;
            res = (x/last + last) / 2;
        }
        return int(res);
    }
};
