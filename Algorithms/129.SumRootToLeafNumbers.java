public class Solution {
    public int sumNumbers(TreeNode root) {
        return sumNumbersToLeaf(root, 0);
    }
    int sumNumbersToLeaf(TreeNode root, int s) {
        if (root == null) {
            return s;
        }
        if (root.left == null && root.right == null) {
            return s*10 + root.val;
        }
        int sum = 0;
        if (root.left != null) {
            sum += sumNumbersToLeaf(root.left, s*10+root.val);
        }
        if (root.right != null) {
            sum += sumNumbersToLeaf(root.right, s*10+root.val);
        }
        return sum;
    }
}
