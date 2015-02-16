public class Solution {
    public int searchInsert(int[] A, int target) {
        int low = 0;
        int high = A.length-1;
        while (low <= high) {
            int middle = low + (high-low)/2;
            if (A[middle] == target) {
                return middle;
            }
            else if (A[middle] < target) {
                low = middle+1;
            }
            else {
                high = middle -1;
            }
        }
        return low;
    }
}
