public class Solution {
    public List<Integer> preorderTraversal(TreeNode root) {
        List<Integer> v = new ArrayList<>();
        Stack<TreeNode> stack = new Stack<>();
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
    /*
    // recursive version
    public List<Integer> preorderTraversal(TreeNode root) {
        List<Integer> v = new ArrayList<>();
        if (root == null) {
            return v;
        }
        v.add(root.val);
        List<Integer> left = preorderTraversal(root.left);
        for (int i=0; i < left.size(); i++) {
            v.add(left.get(i));
        }
        List<Integer> right = preorderTraversal(root.right);
        for (int i=0; i < right.size(); i++) {
            v.add(right.get(i));
        }
        return v;
    }
    */
}
