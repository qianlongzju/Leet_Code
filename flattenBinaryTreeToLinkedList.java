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
    public void flatten(TreeNode root) {
        // Start typing your Java solution below
        // DO NOT write main() function
        flat(root);
    }
    TreeNode flat(TreeNode root) {
        if (root == null) 
            return root;
        if (root.left != null) {
            TreeNode right = root.right;
            TreeNode left = flat(root.left);
            left.right = root.right;
            root.right = root.left;
            root.left = null;
            if (right != null)
                return flat(right);
            else 
                return left;
        } else if (root.right != null) {
            return flat(root.right);
        }
        return root;
    }
}
