import java.util.*;
public class Solution {
    public int search(int[] A, int target) {
        // Start typing your Java solution below
        // DO NOT write main() function
        int left = 0; 
        int right = A.length - 1;
        while (left <= right) {
            int middle = left + (right - left) / 2;
            if (target == A[middle]) {
                return middle;
            } else if (target == A[left]) {
                return left;
            } else if (target == A[right]) {
                return right;
            } else if (A[middle] > A[left]) {
                if (target > A[middle]) {
                    left = middle + 1;
                } else {
                    if (target > A[left]) {
                        right = middle - 1;
                    } else {
                        left = middle + 1;
                    }
                }
            } else {
                if (target < A[middle]) {
                    right = middle - 1;
                } else {
                    if (target > A[right]) {
                        right = middle - 1;
                    } else {
                        left = middle + 1;
                    }
                }
            }
        }
        return -1;
    }
}
