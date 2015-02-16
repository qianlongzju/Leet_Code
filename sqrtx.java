public class Solution {
    public int sqrt(int x) {
        if (x == 0) {
            return 0;
        }
        double last = 0;
        double res = 1;
        while (last != res) {
            last = res;
            res = (x/last + last) / 2;
        }
        return (int)res;
    }
}
