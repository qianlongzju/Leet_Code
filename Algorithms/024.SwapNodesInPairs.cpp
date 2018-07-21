class Solution {
public:
    ListNode *swapPairs(ListNode *head) {
        ListNode *dummyHead = new ListNode(1);
        dummyHead->next = head;
        ListNode *prev = dummyHead;
        ListNode *p = head;
        while (p != NULL && p->next != NULL) {
            ListNode *q = p->next;
            ListNode *r = p->next->next;
            prev->next = q;
            q->next = p;
            p->next = r;
            prev= p;
            p = r;
        }
        return dummyHead->next;
    }
};
