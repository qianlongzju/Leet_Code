class Solution {
public:
    ListNode *addTwoNumbers(ListNode *l1, ListNode *l2) {
        ListNode *dummyHead = new ListNode(0);
        ListNode *current = dummyHead;
        int carry = 0;
        while (l1 != NULL || l2 != NULL) {
            int x = l1 != NULL? l1->val : 0;
            int y = l2 != NULL? l2->val : 0;
            int digit = x + y + carry;
            carry = digit / 10;
            current->next = new ListNode(digit % 10);
            current = current->next;
            if (l1 != NULL) { l1 = l1->next; }
            if (l2 != NULL) { l2 = l2->next; }
        }
        if (carry) { current->next = new ListNode(carry); }
        return dummyHead->next;
    }
};
