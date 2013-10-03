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
    ListNode *mergeTwoLists(ListNode *l1, ListNode *l2) {
        // Start typing your C/C++ solution below
        // DO NOT write int main() function
        ListNode *head = NULL;
        ListNode *p = NULL;
        while (l1 != NULL && l2 != NULL) {
            if (l1->val < l2->val) {
                if (head == NULL) {
                    head = l1;
                    p = l1;
                }
                else {
                    p->next = l1;
                    p = l1;
                }
                l1 = l1->next;
            }
            else {
                if (head == NULL) {
                    head = l2;
                    p = l2;
                }
                else {
                    p->next = l2;
                    p = l2;
                }
                l2 = l2->next;
            }
        }
        if (l1 != NULL) {
            if (head == NULL) {
                head = l1;
            }
            else {
                p->next = l1;
            }
        }
        if (l2 != NULL) {
            if (head == NULL) {
                head = l2;
            }
            else {
                p->next = l2;
            }
        }
        return head;
    }
};
