class Solution {
public:
    int reverse(int x) {
        // Start typing your C/C++ solution below
        // DO NOT write int main() function
        bool positive = true;
        if (x < 0) {
            positive = false;
            x = -x;
        }
        int y = 0;
        while (x) {
            y = (10 * y) + (x % 10);
            x /= 10;
        }
        if (positive)
            return y;
        else
            return -y;
    }
};
