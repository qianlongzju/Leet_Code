/**
 * Definition for binary tree
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */

public class BSTIterator {
    private List<TreeNode> path;
    public BSTIterator(TreeNode root) {
        path = new ArrayList<>();
        while (root != null) {
            path.add(root);
            root = root.left;
        }
    }

    /** @return whether we have a next smallest number */
    public boolean hasNext() {
        return !path.isEmpty();
    }

    /** @return the next smallest number */
    public int next() {
        TreeNode result = path.get(path.size()-1);
        path.remove(path.size()-1);
        TreeNode temp = result.right;
        while (temp != null) {
            path.add(temp);
            temp = temp.left;
        }
        return result.val;
    }
}

/**
 * Your BSTIterator will be called like this:
 * BSTIterator i = new BSTIterator(root);
 * while (i.hasNext()) v[f()] = i.next();
 */
