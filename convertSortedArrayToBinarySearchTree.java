import java.util.*;
/**
 * Definition for binary tree
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class Solution {
    public TreeNode sortedArrayToBST(int[] num) {
        // Start typing your Java solution below
        // DO NOT write main() function
        return sortedSubArrayToBST(num, 0, num.length-1);
    }
    TreeNode sortedSubArrayToBST(int[] num, int start, int end) {
        // Start typing your C/C++ solution below
        // DO NOT write int main() function
        if (start > end) 
            return null;
        int middle = start + (end-start)/2;
        TreeNode root = new TreeNode(num[middle]);
        root.left = sortedSubArrayToBST(num, start, middle-1);
        root.right = sortedSubArrayToBST(num, middle+1, end);
        return root;
    }
}
