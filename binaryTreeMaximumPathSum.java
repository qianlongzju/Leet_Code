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
    public int maxPathSum(TreeNode root) {
        // Start typing your Java solution below
        // DO NOT write main() function
        int[] temp_sum  = new int[1];
        temp_sum[0] = Integer.MIN_VALUE;
        maxPathSum(root, temp_sum); 
        return temp_sum[0];
    }
    int maxPathSum(TreeNode root, int[] max) {
        if (root == null) {
            return 0;
        }
        int left = maxPathSum(root.left, max);
        int right = maxPathSum(root.right, max);
        if (left + right + root.val > max[0]) {
            max[0] = left + right + root.val;
        }
        if (left > right) {
            right = left;
        }
        right = right + root.val;
        if (right > 0) {
            return right;
        }
        return 0;
        
    }
}
