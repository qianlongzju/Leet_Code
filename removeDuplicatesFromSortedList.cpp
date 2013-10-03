/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode *deleteDuplicates(ListNode *head) {
        // Start typing your C/C++ solution below
        // DO NOT write int main() function
        if (head == NULL) {
            return head;
        }
        ListNode *p = head->next;
        ListNode *previous = head;
        while (p != NULL) {
            if (p->val == previous->val) {
                previous->next = p->next;
            }
            else {
                previous = previous->next;
            }
            p = p->next;
        }
        return head;
    }
};
