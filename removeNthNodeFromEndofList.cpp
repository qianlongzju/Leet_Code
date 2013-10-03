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
    ListNode *removeNthFromEnd(ListNode *head, int n) {
        // Start typing your C/C++ solution below
        // DO NOT write int main() function
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
            del->next = del->next->next;
        }
        else {
            head = head->next;
        }
        return head;
        
    }
};
