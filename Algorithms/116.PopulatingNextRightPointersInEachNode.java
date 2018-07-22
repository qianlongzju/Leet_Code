public class Solution {
    public void connect(TreeLinkNode root) {
        if (root == null) {
            return ;
        }
        while (root != null) {
            TreeLinkNode curr_node = root;
            while (curr_node != null) {
                if (curr_node.left != null) 
                    curr_node.left.next = curr_node.right;
                if (curr_node.right != null) {
                    curr_node.right.next = curr_node.next != null ? curr_node.next.left : null;
                }
                curr_node = curr_node.next;
            }
            root = root.left;
        }
    }
    /*
    // not right
    public void connect(TreeLinkNode root) {
        if (root == null) {
            return ;
        }
        Queue<TreeLinkNode> q = new LinkedList<>();
        Queue<TreeLinkNode> next_level_q = new LinkedList<>();
        TreeLinkNode previous = null;
        q.add(root);
        while (q.size() != 0) {
            TreeLinkNode p = q.remove();
            if (previous != null) {
                previous.next = p;
            }
            previous = p;
            if (p.left != null) {
                next_level_q.add(p.left);
            }
            if (p.right != null) {
                next_level_q.add(p.right);
            }
            if (q.size() == 0) {
                p.next = null;
                q = next_level_q;
                next_level_q = new LinkedList<>();
                previous = null;
            }
        }
    }
    */
}
