public class Solution {
    public List<TreeNode> generateTrees(int n) {
        List<TreeNode> result = generateTreesSub(1, n);    
        if (result.size() == 1 && result.get(0) == null) {
            return new ArrayList();
        }
        return result;
    }
    private List<TreeNode> generateTreesSub(int start, int end) {
        List<TreeNode> result = new ArrayList<>();
        if (start > end) {
            result.add(null);
            return result;
        }
        TreeNode root;
        if (start == end) {
            root = new TreeNode(start);
            result.add(root);
            return result;
        }
        for (int i=start; i <= end; i++) {
            List<TreeNode> left = generateTreesSub(start, i-1);
            List<TreeNode> right = generateTreesSub(i+1, end);
            for (int j=0; j< left.size(); j++) {
                for (int k=0; k < right.size(); k++) {
                    root = new TreeNode(i);
                    root.left = left.get(j);
                    root.right = right.get(k);
                    result.add(root);
                }
            }
        }
        return result;
    }
}
