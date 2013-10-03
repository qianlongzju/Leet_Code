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
    ListNode *rotateRight(ListNode *head, int k) {
        // Start typing your C/C++ solution below
        // DO NOT write int main() function
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
