#include "leetcode.h"
class Solution {
public:
    ListNode *partition(ListNode *head, int x) {
        ListNode* leftheadptr = new ListNode(0);
        ListNode* rightheadptr = new ListNode(0);
        ListNode* left = leftheadptr;
        ListNode* right = rightheadptr;
        while (head != NULL) {
            if (head->val < x) {
                left->next = head;
                left = left->next;
            } else {
                right->next = head;
                right = right->next;
            }
            head = head->next;
        }
        left->next = rightheadptr->next;
        right->next = NULL;
        return leftheadptr->next;
    }
};
int main() {
    Solution s;
    ListNode a1 = ListNode(1);
    ListNode a2 = ListNode(4);
    ListNode a3 = ListNode(3);
    ListNode a4 = ListNode(2);
    ListNode a5 = ListNode(5);
    ListNode a6 = ListNode(2);
    a1.next = &a2;
    a2.next = &a3;
    a3.next = &a4;
    a4.next = &a5;
    a5.next = &a6;
    ListNode *v = s.partition(&a1, 3);
    while (v != NULL) {
        cout << v->val << " ";
        v = v->next;
    }
    cout << endl;
    return 0;
}

