class Solution {
    public int findMin(int[] num) {
        int start = 0, end = num.length-1;
        while (start < end && num[start] > num[end]) {
            int mid = start + (end - start) / 2;
            if (num[mid] > num[end]) {
                start = mid + 1;
            } else {
                end = mid;
            }
        }
        return num[start];
    }
}
