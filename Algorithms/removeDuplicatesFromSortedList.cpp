#include "leetcode.h"
class Solution {
public:
    ListNode *deleteDuplicates(ListNode *head) {
        if (head == NULL) {
            return head;
        }
        ListNode *current = head->next;
        ListNode *previous = head;
        while (current != NULL) {
            if (current->val == previous->val) {
                previous->next = current->next;
                ListNode *tmp = current;
                current = current->next;
                delete tmp;
            }
            else {
                previous = previous->next;
                current = current->next;
            }
        }
        return head;
    }
};
