class Solution {
public:
    ListNode *deleteDuplicates(ListNode *head) {
        if (head == NULL)
            return head;
        ListNode *headptr = new ListNode(head->val-1);
        headptr->next = head;
        ListNode *previous = headptr;
        ListNode *p = head;
        bool remove = false;
        while (p != NULL) {
            while (p != NULL && p->next != NULL && p->val == p->next->val) {
                remove = true;
                ListNode *tmp = p;
                p = p->next;
                delete tmp;
            }
            if (remove) {
                previous->next = p->next;
                delete p;
                p = previous->next;
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
