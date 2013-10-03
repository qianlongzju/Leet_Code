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
    public ArrayList<ArrayList<Integer>> pathSum(TreeNode root, int sum) {
        // Start typing your Java solution below
        // DO NOT write main() function
        ArrayList<ArrayList<Integer>> v = new ArrayList<ArrayList<Integer>>();
        ArrayList<Integer> a = new ArrayList<Integer>();
        path_sum(root, sum, a, v);
        return v;
    }
    void path_sum(TreeNode root, int sum, ArrayList<Integer> path, ArrayList<ArrayList<Integer>> v) {
        if (root == null) {
            return;
        }
        ArrayList<Integer> clone_path = (ArrayList<Integer>)path.clone();
        clone_path.add(root.val);
        if (root.left == null && root.right == null && root.val == sum) {
            v.add(clone_path);
            return;
        }
        path_sum(root.left, sum-root.val, clone_path, v);
        path_sum(root.right, sum-root.val, clone_path, v);
        return;
    }
}
