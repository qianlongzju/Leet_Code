class Solution {
    public List<Integer> rightSideView(TreeNode root) {
        List<Integer> result = new ArrayList<>();
        if (root == null)
            return result;
        result.add(root.val);
        List<TreeNode> cur_level = new ArrayList<>();
        List<TreeNode> next_level = new ArrayList<>();
        cur_level.add(root);
        while(cur_level.size() != 0) {
            TreeNode node = cur_level.get(0);
            cur_level.remove(0);
            if (node.left != null) next_level.add(node.left);
            if (node.right != null) next_level.add(node.right);
            if (cur_level.size() == 0) {
                cur_level = next_level;
                next_level = new ArrayList<>();
                if (cur_level.size() != 0)
                    result.add(cur_level.get(cur_level.size()-1).val);
            }
        }
        return result;
    }
}
