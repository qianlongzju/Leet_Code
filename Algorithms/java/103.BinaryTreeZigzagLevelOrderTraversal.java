public class Solution {
    public List<List<Integer>> zigzagLevelOrder(TreeNode root) {
        List<List<Integer>> result = new ArrayList<List<Integer>>();
        if (root == null) {
            return result;
        }
        List<Integer> v = new ArrayList<>();
        List<TreeNode> stack = new ArrayList<>();
        List<TreeNode> next_level_stack = new ArrayList<>();
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
                next_level_stack = new ArrayList<>();
                result.add(v);
                v = new ArrayList<>();
                flag = !flag;
            }
        }
        return result;
    }
}
