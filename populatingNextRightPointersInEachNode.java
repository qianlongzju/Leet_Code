/**
 * Definition for binary tree with next pointer.
 * public class TreeLinkNode {
 *     int val;
 *     TreeLinkNode left, right, next;
 *     TreeLinkNode(int x) { val = x; }
 * }
 */
public class Solution {
    public void connect(TreeLinkNode root) {
        if (root == null) {
            return ;
        }
        ArrayList<TreeLinkNode> stack = new ArrayList<TreeLinkNode>();
        ArrayList<TreeLinkNode> next_level_stack = new ArrayList<TreeLinkNode>();
        TreeLinkNode previous = null;
        stack.add(root);
        while (stack.size() != 0) {
            TreeLinkNode p = stack.get(0);
            if (previous != null) {
                previous.next = p;
            }
            previous = p;
            stack.remove(0);
            if (p.left != null) {
                next_level_stack.add(p.left);
            }
            if (p.right != null) {
                next_level_stack.add(p.right);
            }
            if (stack.size() == 0) {
                p.next = null;
                stack = next_level_stack;
                next_level_stack = new ArrayList<TreeLinkNode>();
                previous = null;
            }
        }
    }
}
