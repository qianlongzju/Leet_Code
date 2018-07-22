class Solution {
public:
    void connect(TreeLinkNode *root) {
        if (root == NULL) {
            return ;
        }
        while (root != NULL) {
            TreeLinkNode *curr_node = root;
            while (curr_node != NULL) {
                if (curr_node->left != NULL) 
                    curr_node->left->next = curr_node->right;
                if (curr_node->right != NULL) {
                    curr_node->right->next = curr_node->next != NULL ? curr_node->next->left : NULL;
                }
                curr_node = curr_node->next;
            }
            root = root->left;
        }
    }
    /*
    // not right
    void connect(TreeLinkNode *root) {
        if (root == NULL) {
            return ;
        }
        queue<TreeLinkNode*> q;
        queue<TreeLinkNode*> next_level_q;
        TreeLinkNode *previous = NULL;
        q.push(root);
        while (!q.empty()) {
            TreeLinkNode *p = q.front();
            if (previous != NULL) {
                previous->next = p;
            }
            previous = p;
            q.pop();
            if (p->left != NULL) {
                next_level_q.push(p->left);
            }
            if (p->right != NULL) {
                next_level_q.push(p->right);
            }
            if (q.empty()) {
                p->next = NULL;
                q.swap(next_level_q);
                previous = NULL;
            }
        }
    }
    */
};
