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
    public int findBottomLeftValue(TreeNode root) {
        List<TreeNode> cur_level = new ArrayList<TreeNode>();
        List<TreeNode> next_level = new ArrayList<TreeNode>();
        cur_level.add(root);
        int value = root.val;
        while(cur_level.size() > 0) {
            TreeNode node = cur_level.get(0);
            cur_level.remove(0);
            if (node.left != null) next_level.add(node.left);
            if (node.right != null) next_level.add(node.right);
            if (cur_level.size() == 0) {
                cur_level = next_level;
                if (cur_level.size() != 0)
                    value = cur_level.get(0).val;
                next_level = new ArrayList<TreeNode>();
            }
        }
        return value;
    }
}
