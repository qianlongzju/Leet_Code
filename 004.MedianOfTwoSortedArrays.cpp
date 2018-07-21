class Solution {
public:
    double findMedianSortednums1rrays(vector<int>& nums1, vector<int>& nums2) {
        int m = nums1.size();
        int n = nums2.size();
        int total = m + n;
        if (total & 0x1)
            return find_kth(nums1, m, nums2, n, (total >> 2) + 1);
        else
            return (find_kth(nums1, m, nums2, n, total >> 2)
                    + find_kth(nums1, m, nums2, n, (total >> 2) + 1)) / 2;
    }
private:
    static double find_kth(vector<int>& nums1, int m, vector<int>& nums2, int n, int k) {
        //always assume that m is equal or smaller than n
        if (m > n) return find_kth(nums2, n, nums1, m, k);
        if (m == 0) return nums2[k - 1];
        if (k == 1) return min(nums1[0], nums2[0]);
        //divide k into two parts
        int pa = min(k >> 1, m), pb = k - pa;
        if (nums1[pa - 1] < nums2[pb - 1])
            return find_kth(nums1 + pa, m - pa, nums2, n, k - pa);
        else if (nums1[pa - 1] > nums2[pb - 1])
            return find_kth(nums1, m, nums2 + pb, n - pb, k - pb);
        else
            return nums1[pa - 1];
    }
};
