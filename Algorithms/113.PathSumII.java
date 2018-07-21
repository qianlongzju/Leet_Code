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
    public ArrayList<ArrayList<Integer>> pathSum(TreeNode root, int sum) {
        ArrayList<ArrayList<Integer>> result = new ArrayList<ArrayList<Integer>>();
        ArrayList<Integer> path = new ArrayList<Integer>();
        path_sum(root, sum, path, result);
        return result;
    }
    void path_sum(TreeNode root, int sum, ArrayList<Integer> path, ArrayList<ArrayList<Integer>> result) {
        if (root == null) {
            return;
        }
        path.add(root.val);
        if (root.left == null && root.right == null && root.val == sum) {
            result.add((ArrayList<Integer>)path.clone());
            path.remove(path.size()-1);
            return;
        }
        path_sum(root.left, sum-root.val, path, result);
        path_sum(root.right, sum-root.val, path, result);
        path.remove(path.size()-1);
    }
}
