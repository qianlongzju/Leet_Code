public class Solution {
    public boolean isValidBST(TreeNode root) {
        return validBST(root, null, null);
    }
    boolean validBST(TreeNode root, Integer min, Integer max) {
        if (root == null)
            return true;
        if (min != null && min >= root.val)
            return false;
        if (max != null && max <= root.val)
            return false;
        return validBST(root.left, min, root.val) 
            && validBST(root.right, root.val, max);
    }
}
