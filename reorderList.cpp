#include "leetcode.h"
class Solution {
public:
    void reorderList(ListNode *head) {
        // IMPORTANT: Please reset any member data you declared, as
        // the same Solution instance will be reused for each test case.
        ListNode* p = split(head);
        //print(head);
        //print(p);
        p = reverse(p);
        //print(p);
        head = merge(head, p);
    }
    void print(ListNode *head) {
        ListNode *p = head;
        cout << "start print" << endl;
        while (p != NULL) {
            cout << p->val << " ";
            p = p->next;
        }
        cout << endl << "end print" << endl;
    }
    ListNode* split(ListNode *head) {
        if (head == NULL) 
            return head;
        ListNode *slow = head;
        ListNode *fast = head->next;
        while (fast != NULL && fast->next != NULL) {
            slow = slow->next;
            fast = fast->next->next;
        }
        ListNode *p = slow->next;
        slow->next = NULL;
        return p;
    }
    ListNode* reverse(ListNode *head) { 
        ListNode *headptr = new ListNode(0);
        while (head != NULL) {
            ListNode *tmp = head->next;
            head->next = headptr->next;
            headptr->next = head;
            head = tmp;
        }
        return headptr->next;
    }
    ListNode* merge(ListNode *p, ListNode *q) {
        ListNode *head = new ListNode(0);
        ListNode *tmp = head;
        while (p != NULL && q != NULL) {
            tmp->next = p;
            p = p->next;
            tmp = tmp->next;
            tmp->next = q;
            q = q->next;
            tmp = tmp->next;
        }
        if (p != NULL) {
            tmp->next = p;
        }
        return head->next;
    }
};
int main() {
    Solution s;
    ListNode a = ListNode(1);
    ListNode b = ListNode(2);
    ListNode c = ListNode(3);
    ListNode d = ListNode(4);
    a.next = &b;
    b.next = &c;
    //c.next = &d;
    ListNode * head = &a;
    s.reorderList(head);
    while (head != NULL) {
        cout << head->val << endl;
        head = head->next;
    }
    return 0;
}
