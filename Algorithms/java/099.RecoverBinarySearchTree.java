public class Solution {
    TreeNode pre, node1, node2;
    public void recoverTree(TreeNode root) {
        pre = null;
        node1 = null;
        node2 = null;
        recoverTreeRecursive(root);
        int temp = node1.val;
        node1.val = node2.val;
        node2.val = temp;
    }
    private void recoverTreeRecursive(TreeNode root) {
        if (root == null) {
            return;
        }
        recoverTreeRecursive(root.left);
        if (pre != null && root.val < pre.val) {
            if (node1 == null) {
                node1 = pre;
                node2 = root;
            } else {
                node2 = root;
            }
        }
        pre = root;
        recoverTreeRecursive(root.right);
    }
}
