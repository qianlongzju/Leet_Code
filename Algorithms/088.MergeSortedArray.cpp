class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        int C[m+n];
        int i = 0;
        int j = 0;
        int k = 0;
        while (i < m && j < n) {
            if (nums1[i] < nums2[j]) {
                C[k++] = nums1[i++];
            }
            else {
                C[k++] = nums2[j++];
            }
        }
        while (i < m) {
            C[k++] = nums1[i++];
        }
        while (j < n) {
            C[k++] = nums2[j++];
        }
        k = 0;
        while (k < (m+n)) {
            nums1[k] = C[k];
            k++;
        }
    }
};
