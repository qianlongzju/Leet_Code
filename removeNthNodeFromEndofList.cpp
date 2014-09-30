#include "leetcode.h"
class Solution {
public:
    ListNode *removeNthFromEnd(ListNode *head, int n) {
        int index = 0;
        ListNode *p = head;
        ListNode *del = NULL;
        while (p != NULL) {
            p = p->next;
            if (del != NULL) {
                del = del->next;
            }
            index ++;
            if (index == n+1) {
                del = head;
            }
        }
        if (index >= n+1) {
            ListNode *tmp = del->next;
            del->next = del->next->next;
            delete tmp;
        }
        else {
            ListNode *tmp = head;
            head = head->next;
            delete tmp;
        }
        return head;
    }
};
