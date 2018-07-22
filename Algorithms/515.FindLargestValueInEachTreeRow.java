/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    public List<Integer> largestValues(TreeNode root) {
        List<Integer> result = new ArrayList<>();
        if (root == null) return result;
        List<TreeNode> cur_level = new ArrayList<>();
        List<TreeNode> next_level = new ArrayList<>();
        cur_level.add(root);
        int maximum = root.val;
        while(cur_level.size() != 0) {
            TreeNode node = cur_level.get(0);
            cur_level.remove(0);
            maximum = Math.max(maximum, node.val);
            if (node.left != null) next_level.add(node.left);
            if (node.right != null) next_level.add(node.right);
            if (cur_level.size() == 0) {
                result.add(maximum);
                if (next_level.size() == 0) break;
                cur_level = next_level;
                next_level = new ArrayList<>();
                maximum = cur_level.get(0).val;
            }
        }
        return result;
    }
}
