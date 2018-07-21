class Solution {
public:
    ListNode *rotateRight(ListNode *head, int k) {
        if (head == NULL) {
            return head;
        }
        ListNode *p = head;
        int count = 0;
        while (p != NULL) {
            p = p->next;
            count ++;
        }
        k = k % count;
        if (k == 0) {
            return head;
        }
        p = head;
        ListNode *q = NULL;
        ListNode *r;
        count = 0;
        while (p != NULL) {
            r = p;
            p = p->next;
            count ++;
            if (q != NULL) {
                q = q->next;
            }
            if (count == k+1) {
                q = head;
            }
        }
        r->next = head;
        head = q->next;
        q->next = NULL;
        return head;
    }
};
