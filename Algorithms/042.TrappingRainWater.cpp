class Solution {
public:
    int trap(int A[], int n) {
        int leftToRight[n];
        int rightToLeft[n];
        leftToRight[0] = 0;
        rightToLeft[n-1] = 0;
        for (int i = 1; i < n; ++i) {
            leftToRight[i] = max(leftToRight[i-1], A[i-1]);
            rightToLeft[n-i-1] = max(rightToLeft[n-i], A[n-i]);
        }
        int total = 0;
        for (int i=1; i < n-1; i++) {
            int height = min(leftToRight[i], rightToLeft[i]);
            if (height > A[i]) 
                total += height - A[i];
        }
        return total;
    }
};
int main() {
    Solution s;
    int a[] = {0,1,0,2,1,0,1,3,2,1,2,1};
    cout << s.trap(a, 12) << endl;
    int b[] = {4, 2, 0, 3, 2, 5};
    cout << s.trap(b, 6) << endl;
    return 0;
}
