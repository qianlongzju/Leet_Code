#include "leetcode.h"
class Solution {
public:
    TreeNode *sortedListToBST(ListNode *head) {
        int length = 0;
        ListNode* p = head;
        while (p != NULL) {
            length ++;
            p = p->next;
        }
        return sortedListToBST(head, 0, length-1);
    }

    TreeNode* sortedListToBST(ListNode* &list, int start, int end) {
        if (start > end) return NULL;
        int mid = start + (end - start) / 2;
        TreeNode *leftChild = sortedListToBST(list, start, mid-1);
        TreeNode *parent = new TreeNode(list->val);
        parent->left = leftChild;
        list = list->next;
        parent->right = sortedListToBST(list, mid+1, end);
        return parent;
    } 
    /*
    TreeNode *sortedListToBST(ListNode *head) {
        if (head == NULL) {
            return NULL;
        }
        if (head->next == NULL) {
            return new TreeNode(head->val);
        }
        ListNode* slow = head;
        ListNode* fast = head->next->next;
        while (fast != NULL && fast->next != NULL) {
            fast = fast->next->next;
            slow = slow->next;
        }
        TreeNode* root = new TreeNode(slow->next->val);
        root->right = sortedListToBST(slow->next->next);
        slow->next = NULL;
        root->left = sortedListToBST(head);
        return root;
    }
    */
};
int main() {
    Solution s;
    ListNode* head = new ListNode(1);
    s.sortedListToBST(head);

    return 0;
}
