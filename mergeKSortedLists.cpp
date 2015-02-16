#include "leetcode.h"
class Solution {
public:
    ListNode *mergeKLists(vector<ListNode *> &lists) {
        if (lists.size() == 0) {
            return NULL;
        }
        if (lists.size() == 1) {
            return lists[0];
        }
        ListNode *p = lists[0];
        for (int i=1; i < lists.size(); ++i) {
            p = mergeTwoLists(p, lists[i]);
        }
        return p;
    }
    ListNode *mergeTwoLists(ListNode *l1, ListNode *l2) {
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
int main() {
    Solution s;

    return 0;
}

