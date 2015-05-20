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
    public List<Integer> inorderTraversal(TreeNode root) {
        List<Integer> v = new ArrayList<Integer>();
        Stack<TreeNode> stack = new Stack<TreeNode>();
        TreeNode p = root;
        while (stack.size() != 0 || p != null) {
            if (p != null) {
                stack.add(p);
                p = p.left;
            }
            else {
                p = stack.peek();
                stack.pop();
                v.add(p.val);
                p = p.right;
            }
        }
        return v;
    }
    public List<Integer> inorderTraversal_recursive(TreeNode root) {
        List<Integer> v = new ArrayList<Integer>();
        if (root == null) {
            return v;
        }
        ArrayList<Integer> left = inorderTraversal_recursive(root.left);
        for (int i=0; i < left.size(); i++) {
            v.add(left.get(i));
        }
        v.add(root.val);
        ArrayList<Integer> right = inorderTraversal_recursive(root.right);
        for (int i=0; i < right.size(); i++) {
            v.add(right.get(i));
        }
        return v;
    }
}
