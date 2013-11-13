#include "leetcode.h"
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<string> vs;
typedef pair<int, int> ii;
typedef vector<ii> vii;
typedef vector< pair<double,ii> > vdii;
#define sz(a) int((a).size())
#define pb push_back
#define all(c) (c).begin(),(c).end()
#define tr(c,i) for(typeof((c).begin()) i = (c).begin(); i != (c).end(); i++)
#define present(c,x) ((c).find(x) != (c).end())
#define cpresent(c,x) (find(all(c),x) != (c).end())
using namespace std;
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

