#include "leetcode.h"
class Solution {
public:
    ListNode *swapPairs(ListNode *head) {
        if (head == NULL || head->next == NULL) {
            return head;
        }
        ListNode *p = head;
        head = head->next;
        p->next = head->next;
        head->next = p;
        ListNode *q = p->next;
        while (q != NULL && q->next != NULL) {
            ListNode *r = q->next;
            q->next = q->next->next;
            r->next = q;
            p->next = r;
            p = p->next->next;
            q = q->next;
        }
        return head;
    }
};
