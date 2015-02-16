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
    public boolean isValidBST(TreeNode root) {
        return validBST(root, false, 0, false, 0);
    }
    boolean validBST(TreeNode root, boolean minBound, int min, boolean maxBound, int max) {
        boolean result = false;
        if (root == null) {
            return true;
        }
        if (minBound) {
            if (min >= root.val) {
                return false;
            }
        }
        if (maxBound) {
            if (max <= root.val) {
                return false;
            }
        }
        if (root.left == null && root.right == null) {
            return true;
        }
        if (root.left == null && root.right != null) {
            result = validBST(root.right, true, root.val, maxBound, max);
        }
        if (root.left != null && root.right == null) {
            result = validBST(root.left, minBound, min, true, root.val);
        }
        if (root.left != null && root.right != null) {
            result = validBST(root.left, minBound, min, true, root.val) && validBST(root.right, true, root.val, maxBound, max);
        }
        return result;
    }
}
