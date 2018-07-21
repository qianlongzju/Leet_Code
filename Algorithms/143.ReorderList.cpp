class Solution {
public:
    void reorderList(ListNode *head) {
        ListNode* p = split(head);
        p = reverse(p);
        head = merge(head, p);
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
