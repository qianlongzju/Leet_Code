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
    ListNode* removeElements(ListNode* head, int val) {
        ListNode *dummyHead = new ListNode(0);
        dummyHead->next = head;
        ListNode *previous = dummyHead;
        ListNode *current = head;
        while(current != NULL) {
            if (current->val == val) {
                previous->next = current->next;
                delete current;
                current = current->next;
            } else {
                previous = previous->next;
                current = current->next;
            }
        }
        return dummyHead->next;
    }
};
