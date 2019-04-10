class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        int total = nums1.size() + nums2.size();
        if (total & 0x1)
            return find_kth(nums1, nums2, (total >> 1) + 1);
        else
            return (find_kth(nums1, nums2, total >> 1)
                    + find_kth(nums1, nums2, (total >> 1) + 1)) / 2;
    }
private:
    static double find_kth(vector<int>& nums1, vector<int>& nums2, int k) {
        //always assume that m is equal or smaller than n
        int m = nums1.size();
        int n = nums2.size();
        if (m > n) return find_kth(nums2, nums1, k);
        if (m == 0) return nums2[k - 1];
        if (k == 1) return min(nums1[0], nums2[0]);
        //divide k into two parts
        int pa = min(k >> 1, m), pb = k - pa;
        if (nums1[pa - 1] < nums2[pb - 1]) {
            vector<int> new_nums1(nums1.begin() + pa, nums1.end());
            return find_kth(new_nums1, nums2, k - pa);
        }
        else if (nums1[pa - 1] > nums2[pb - 1]) {
            vector<int> new_nums2(nums2.begin() + pb, nums2.end());
            return find_kth(nums1, new_nums2, k - pb);
        }
        else
            return nums1[pa - 1];
    }
};
