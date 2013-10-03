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
    ListNode *reverseBetween(ListNode *head, int m, int n) {
        // Start typing your C/C++ solution below
        // DO NOT write int main() function
        if (m == n) {
            return head;
        }
        ListNode *headptr = new ListNode(0);
        headptr->next = head;
        ListNode *ins = headptr;
        ListNode *p = head;
        for (int i=1; i < n; i++) {
            if (i < m) {
                ins = ins->next;
                p = p->next;
            }
            else {
                ListNode *temp = p->next;
                p->next = temp->next;
                temp->next = ins->next;
                ins->next = temp;
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
    ListNode *l4 = new ListNode(4);
    ListNode *l5 = new ListNode(5);
    l1->next = l2;
    l2->next = l3;
    l3->next = l4;
    l4->next = l5;
    l5->next = NULL;
    ListNode *head = s.reverseBetween(l1, 2, 4);
    while (head != NULL) {
        cout << head->val << endl;
        head = head->next;
    }
    return 0;
}
