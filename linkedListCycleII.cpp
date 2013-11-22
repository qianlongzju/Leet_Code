#include "leetcode.h"
class Solution {
public:
    ListNode *detectCycle(ListNode *head) {
        // IMPORTANT: Please reset any member data you declared, as
        // the same Solution instance will be reused for each test case.
        if (head == NULL)
            return NULL;
        ListNode *slow = head;
        ListNode *fast = head;
        while (fast != NULL && fast->next != NULL) {
            slow = slow->next;
            fast = fast->next->next;
            if (fast == slow) {
                break;
            }
        }
        if (fast == NULL || fast->next == NULL) 
            return NULL;
        slow = head;
        while (slow != fast) {
            slow = slow->next;
            fast = fast->next;
        }
        return fast;
    }
};
int main() {
    Solution s;
    ListNode *head = new ListNode(1);
    ListNode *a = new ListNode(2);
    head->next = a;
    a->next = head;
    ListNode *result = s.detectCycle(head);
    if (result != NULL) 
        cout << result->val << endl;
    else 
        cout << "no cycle" << endl;
    return 0;
}
