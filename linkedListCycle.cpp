#include "leetcode.h"
class Solution {
public:
    bool hasCycle(ListNode *head) {
        // IMPORTANT: Please reset any member data you declared, as
        // the same Solution instance will be reused for each test case.
        if (head == NULL)
            return false;
        ListNode *slow = head;
        ListNode *fast = head;
        while (fast != NULL && fast->next != NULL) {
            slow = slow->next;
            fast = fast->next->next;
            if (fast == slow) {
                break;
            }
        }
        //if (slow == fast && slow->next != NULL) 
        //    return true;
        //else 
        //    return false;
        if (fast == NULL || fast->next == NULL) 
            return false;
        return true;
    }
    //bool hasCycle(ListNode *head) {
    //    // IMPORTANT: Please reset any member data you declared, as
    //    // the same Solution instance will be reused for each test case.
    //    if (head == NULL)
    //        return false;
    //    ListNode *slow = head;
    //    ListNode *fast = head->next;
    //    while (fast != NULL && fast != slow) {
    //        if (fast->next == NULL)
    //            break;
    //        slow = slow->next;
    //        fast = fast->next->next;
    //    }
    //    if (slow == fast) 
    //        return true;
    //    else 
    //        return false;
    //}
};
int main() {
    Solution s;

    return 0;
}

