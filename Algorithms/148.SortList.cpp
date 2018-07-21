class Solution {
public:
    ListNode *sortList(ListNode *head) {
        // IMPORTANT: Please reset any member data you declared, as
        // the same Solution instance will be reused for each test case.
        int totalLength = genLength(head);
        if (totalLength == 0 || totalLength == 1) 
            return head;
        int leftLength = totalLength / 2;
        ListNode *leftHead = head;
        ListNode *rightHead = getRightHead(head, leftLength);
        leftHead = sortList(leftHead);
        rightHead = sortList(rightHead);
        return merge(leftHead, rightHead);
    }
    ListNode *getRightHead(ListNode *head, int leftLength) {
        ListNode *rightHead = head;
        int i = 1;
        while (i < leftLength) {
            rightHead = rightHead->next;
            i ++;
        }
        ListNode *p = rightHead->next;
        rightHead->next = NULL;
        rightHead = p;
        return rightHead;
    }
    ListNode *merge(ListNode *leftHead, ListNode *rightHead) {
        ListNode *headptr = new ListNode(0);
        ListNode *p = headptr;
        while (leftHead != NULL && rightHead != NULL) {
            if (leftHead->val < rightHead->val) {
                p->next = leftHead;
                leftHead = leftHead->next;
            } else {
                p->next = rightHead;
                rightHead = rightHead->next;
            }
            p = p->next;
        }
        if (leftHead != NULL)
            p->next = leftHead;
        if (rightHead != NULL) 
            p->next = rightHead;
        return headptr->next;
    }
    int genLength(ListNode *head) {
        ListNode *p = head;
        int n = 0;
        while (p != NULL) {
            n++;
            p = p->next;
        }
        return n;
    }
};
