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
    public ArrayList<Integer> preorderTraversal(TreeNode root) {
        ArrayList<Integer> v = new ArrayList<Integer>();
        Stack<TreeNode> stack = new Stack<TreeNode>();
        TreeNode p = root;
        while (!stack.empty() || p != null) {
            if (p != null) {
                v.add(p.val);
                if (p.right != null)
                    stack.push(p.right);
                p = p.left;
            }
            else {
                p = stack.peek();
                stack.pop();
            }
        }
        return v;
    }
    // recursive version
    //public ArrayList<Integer> preorderTraversal(TreeNode root) {
    //    // IMPORTANT: Please reset any member data you declared, as
    //    // the same Solution instance will be reused for each test case.
    //    ArrayList<Integer> v = new ArrayList<Integer>();
    //    if (root == null) {
    //        return v;
    //    }
    //    v.add(root.val);
    //    ArrayList<Integer> left = preorderTraversal(root.left);
    //    for (int i=0; i < left.size(); i++) {
    //        v.add(left.get(i));
    //    }
    //    ArrayList<Integer> right = preorderTraversal(root.right);
    //    for (int i=0; i < right.size(); i++) {
    //        v.add(right.get(i));
    //    }
    //    return v;
    //}
}
