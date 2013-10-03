#include <iostream>
using namespace std;
 struct ListNode {
     int val;
     ListNode *next;
     ListNode(int x) : val(x), next(NULL) {}
 };
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
        ListNode *headptr = new ListNode(head->val-1);
        headptr->next = head;
        ListNode *previous = headptr;
        ListNode *p = head;
        bool remove = false;
        while (p != NULL) {
            while (p != NULL && p->next != NULL && p->val == p->next->val) {
                remove = true;
                p = p->next;
            }
            if (remove) {
                previous->next = p->next;
                p = p->next;
                remove = false;
            }
            else {
                p = p->next;
                previous = previous->next;
            }
        }
        return headptr->next;
    }
};
int main() {
    Solution s;
    ListNode *l1 = new ListNode(1);
    ListNode *l2 = new ListNode(2);
    ListNode *l3 = new ListNode(3);
    ListNode *l4 = new ListNode(3);
    ListNode *l5 = new ListNode(4);
    ListNode *l6 = new ListNode(4);
    ListNode *l7 = new ListNode(5);
    l1->next = l2;
    l2->next = l3;
    l3->next = l4;
    l4->next = l5;
    l5->next = l6;
    l6->next = l7;
    l7->next = NULL;
    ListNode *head = s.deleteDuplicates(l1);
    while (head != NULL) {
        cout << head->val << endl;
        head = head->next;
    }
    return 0;
}
