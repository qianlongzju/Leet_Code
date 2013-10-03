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
    public boolean isBalanced(TreeNode root) {
        // Start typing your Java solution below
        // DO NOT write main() function
        if (height(root) == -1) {
            return false;
        }
        else {
            return true;
        }
    }
    int height(TreeNode root) {
        if (root == null) {
            return 0;
        }
        else {
            int left = height(root.left);
            if (left == -1) {
                return -1;
            }
            int right = height(root.right);
            if (right == -1) {
                return -1;
            }
            if (left == right && left >= 0) {
                return 1+left;
            }
            else if (left+1 == right && left >= 0) {
                return 1 + right;
            }
            else if (right+1 == left && right >= 0) {
                return 1 + left;
            }
            else {
                return -1;
            }
        }
    }
}
