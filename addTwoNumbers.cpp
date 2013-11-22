#include "leetcode.h"
class Solution {
public:
    ListNode *addTwoNumbers(ListNode *l1, ListNode *l2) {
        // Start typing your C/C++ solution below
        // DO NOT write int main() function
        ListNode *head = NULL;
        ListNode *previous = head;
        int q = 0;
        while (l1 != NULL && l2 != NULL) {
            int p = q + l1->val + l2->val;
            q = p / 10;
            p = p % 10;
            ListNode *a = new ListNode(p);
            if (head == NULL) {
                head = a;
                previous = a;
            }
            else {
                previous->next = a;
                previous = a;
            }
            l1 = l1->next;
            l2 = l2->next;
        }
        while (l1 != NULL) {
            int p = q + l1->val;
            q = p / 10;
            p = p % 10;
            ListNode *a = new ListNode(p);
            if (head == NULL) {
                head = a;
                previous = a;
            }
            else {
                previous->next = a;
                previous = a;
            }
            l1 = l1->next;
        }
        while (l2 != NULL) {
            int p = q + l2->val;
            q = p / 10;
            p = p % 10;
            ListNode *a = new ListNode(p);
            if (head == NULL) {
                head = a;
                previous = a;
            }
            else {
                previous->next = a;
                previous = a;
            }
            l2 = l2->next;
        }
        if (q) {
            ListNode *a = new ListNode(q);
            previous->next = a;
        }
        return head;
    }
};
