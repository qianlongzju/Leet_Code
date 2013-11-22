#include "leetcode.h"
class Solution {
public:
    ListNode *reverseKGroup(ListNode *head, int k) {
        // Start typing your C/C++ solution below
        // DO NOT write int main() function
        if (k < 2 || head == NULL) {
            return head;
        }
        ListNode *headptr = new ListNode(0);
        headptr->next = head;
        ListNode *previous = headptr;
        ListNode *p = head;
        ListNode *pp = head;
        int count = 1;
        while (pp != NULL) {
            if (count == k) {
                pp = pp->next;
                while(p->next != pp) {
                    ListNode *temp = p->next;
                    p->next = temp->next;
                    temp->next = previous->next;
                    previous->next = temp;
                }
                previous = p;
                p = p->next;
                count = 1;
            }
            else {
                pp = pp->next;
                count ++;
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
    ListNode *l4 = new ListNode(4);
    ListNode *l5 = new ListNode(5);
    l1->next = l2;
    l2->next = l3;
    l3->next = l4;
    l4->next = l5;
    l5->next = NULL;
    ListNode *head = s.reverseKGroup(l1, 2);
    while (head != NULL) {
        cout << head->val << endl;
        head = head->next;
    }
    return 0;
}
