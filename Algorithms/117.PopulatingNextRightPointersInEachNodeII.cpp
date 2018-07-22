class Solution {
public:
    void connect(TreeLinkNode *root) {
        if (root == NULL) return;
        while (root != NULL) {
            TreeLinkNode* start = nextLevelFirstNode(root);
            TreeLinkNode* curr_node = start;
            while (curr_node != NULL) {
                TreeLinkNode* next_node = nextLevelNextNode(root, curr_node);
                curr_node->next = next_node;
                curr_node = next_node;
            }
            root = start;
        }
    }

private:
    TreeLinkNode* nextLevelFirstNode(TreeLinkNode *root) {
        if (root == NULL) return NULL;
        if (root->left != NULL) return root->left;
        return nextLevelNextNode(root, root->left);
    }

    TreeLinkNode* nextLevelNextNode(TreeLinkNode* root, TreeLinkNode* curr_node) {
        if (root->left == curr_node && root->right != NULL) {
            return root->right;
        }
        while (root->next != NULL) {
            root = root->next;
            if (root->left != NULL) return root->left;
            if (root->right != NULL) return root->right;
        }
        return NULL;
    }
};
