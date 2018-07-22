public class Solution {
    public List<List<Integer>> pathSum(TreeNode root, int sum) {
        List<List<Integer>> result = new ArrayList<List<Integer>>();
        List<Integer> path = new ArrayList<>();
        path_sum(root, sum, path, result);
        return result;
    }
    void path_sum(TreeNode root, int sum, List<Integer> path, List<List<Integer>> result) {
        if (root == null) {
            return;
        }
        path.add(root.val);
        if (root.left == null && root.right == null && root.val == sum) {
            result.add(new ArrayList<>(path));
            path.remove(path.size()-1);
            return;
        }
        path_sum(root.left, sum-root.val, path, result);
        path_sum(root.right, sum-root.val, path, result);
        path.remove(path.size()-1);
    }
}
