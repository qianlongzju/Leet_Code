public class Solution {
    public List<TreeNode> generateTrees(int n) {
        return generateTreesSub(1, n);    
    }
    private List<TreeNode> generateTreesSub(int start, int end) {
        List<TreeNode> result = new ArrayList<TreeNode>();
        if (start > end) {
            result.add(null);
            return result;
        }
        TreeNode root = null;
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
