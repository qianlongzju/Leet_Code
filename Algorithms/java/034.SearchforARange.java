public class Solution {
    public int[] searchRange(int[] A, int target) {
        int[] v = new int[2];
        if (A.length == 0) {
            v[0] = -1;
            v[1] = -1;
            return v;
        }
        int low = 0;
        int high = A.length-1;
        int middle = 0;
        while (low <= high) {
            middle = low + (high-low)/2;
            if (A[middle] < target) {
                low = middle + 1;
            }
            else if (A[middle] > target) {
                high = middle - 1;
            }
            if (A[middle] == target) {
                break;
            }
        }
        if (A[middle] != target) {
            v[0] = -1;
            v[1] = -1;
            return v;
        }
        low = middle;
        while (low >= 0 && A[low] == target) {
            low --;
        }
        v[0] = low+1;
        high = middle;
        while (high < A.length && A[high] == target) {
            high ++;
        }
        v[1] = high-1;
        return v;
    }
}
