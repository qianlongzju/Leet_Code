#include "leetcode.h"
class Solution {
public:
    ListNode *deleteDuplicates(ListNode *head) {
        if (head == NULL)
            return head;
        ListNode *headptr = new ListNode(head->val-1);
        headptr->next = head;
        ListNode *previous = headptr;
        ListNode *p = head;
        bool remove = false;
        while (p != NULL) {
            while (p != NULL && p->next != NULL && p->val == p->next->val) {
                remove = true;
                ListNode *tmp = p;
                p = p->next;
                delete tmp;
            }
            if (remove) {
                previous->next = p->next;
                delete p;
                p = previous->next;
                remove = false;
            }
            else {
                p = p->next;
                previous = previous->next;
            }
        }
        return headptr->next;
    }
};
int main() {
    Solution s;
    ListNode *l1 = new ListNode(1);
    ListNode *l2 = new ListNode(2);
    ListNode *l3 = new ListNode(3);
    ListNode *l4 = new ListNode(3);
    ListNode *l5 = new ListNode(4);
    ListNode *l6 = new ListNode(4);
    ListNode *l7 = new ListNode(5);
    l1->next = l2;
    l2->next = l3;
    l3->next = l4;
    l4->next = l5;
    l5->next = l6;
    l6->next = l7;
    l7->next = NULL;
    ListNode *head = s.deleteDuplicates(l1);
    while (head != NULL) {
        cout << head->val << endl;
        head = head->next;
    }
    return 0;
}
