public class Solution {
    private TreeLinkNode root;
    public void connect(TreeLinkNode root) {
        if (root == null) return;
        this.root = root;
        while (this.root != null) {
            TreeLinkNode start = nextLevelFirstNode();
            TreeLinkNode curr_node = start;
            while (curr_node != null) {
                TreeLinkNode next_node = nextLevelNextNode(curr_node);
                curr_node.next = next_node;
                curr_node = next_node;
            }
            this.root = start;
        }
    }

    private TreeLinkNode nextLevelFirstNode() {
        if (root == null) return null;
        if (root.left != null) return root.left;
        return nextLevelNextNode(root.left);
    }

    private TreeLinkNode nextLevelNextNode(TreeLinkNode curr_node) {
        if (root.left == curr_node && root.right != null) {
            return root.right;
        }
        while (root.next != null) {
            root = root.next;
            if (root.left != null) return root.left;
            if (root.right != null) return root.right;
        }
        return null;
    }
}
