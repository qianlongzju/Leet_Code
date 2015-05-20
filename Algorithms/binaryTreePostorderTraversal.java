public class Solution {
    public List<Integer> postorderTraversal(TreeNode root) {
        List<Integer> v = new ArrayList<Integer>();
        if (root == null)
            return v;
        Stack<TreeNode> stack = new Stack<TreeNode>();
        stack.push(root);
        TreeNode prevNode = null;
        while (!stack.empty()) {
            TreeNode currNode = stack.peek();
            if (prevNode == null || prevNode.left == currNode || 
                    prevNode.right == currNode) {
                if (currNode.left != null) 
                    stack.push(currNode.left);
                else if (currNode.right != null) {
                    stack.push(currNode.right);
                }
            }
            else if (currNode.left == prevNode) {
                if (currNode.right != null)
                    stack.push(currNode.right);
            }
            else {
                v.add(currNode.val);
                stack.pop();
            }
            prevNode = currNode;
        }
        return v;
    }

    /*
    // recursive version
    public List<Integer> postorderTraversal(TreeNode root) {
        List<Integer> v = new ArrayList<Integer>();
        if (root == null) {
            return v;
        }
        List<Integer> left = postorderTraversal(root.left);
        for (int i=0; i < left.size(); i++) {
            v.add(left.get(i));
        }
        List<Integer> right = postorderTraversal(root.right);
        for (int i=0; i < right.size(); i++) {
            v.add(right.get(i));
        }
        v.add(root.val);
        return v;
    }
    */
}
