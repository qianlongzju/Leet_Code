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
    public ArrayList<ArrayList<Integer>> zigzagLevelOrder(TreeNode root) {
        ArrayList<ArrayList<Integer>> result = new ArrayList<ArrayList<Integer>>();
        if (root == null) {
            return result;
        }
        ArrayList<Integer> v = new ArrayList<Integer>();
        ArrayList<TreeNode> stack = new ArrayList<TreeNode>();
        ArrayList<TreeNode> next_level_stack = new ArrayList<TreeNode>();
        stack.add(root);
        boolean flag = false;
        while (stack.size() != 0) {
            TreeNode p = stack.get(0);
            stack.remove(0);
            if (flag) {
                v.add(0, p.val);
            }
            else {
                v.add(p.val);
            }
            if (p.left != null) {
                next_level_stack.add(p.left);
            }
            if (p.right != null) {
                next_level_stack.add(p.right);
            }
            if (stack.size() == 0) {
                stack = next_level_stack;
                next_level_stack = new ArrayList<TreeNode>();
                result.add(v);
                v = new ArrayList<Integer>();
                flag = !flag;
            }
        }
        return result;
    }
}
