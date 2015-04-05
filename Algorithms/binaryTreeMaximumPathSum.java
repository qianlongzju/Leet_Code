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
    private int max_path_sum;
    public int maxPathSum(TreeNode root) {
        max_path_sum = Integer.MIN_VALUE;
        maxSum(root);
        return max_path_sum;
    }
    private int maxSum(TreeNode root) {
        if (root == null) return 0;
        int left = maxSum(root.left);
        int right = maxSum(root.right);
        max_path_sum = Math.max(max_path_sum, left + right + root.val);
        int ret = root.val + Math.max(left, right);
        return ret > 0? ret:0;
    }
}
