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
    ListNode *mergeKLists(vector<ListNode *> &lists) {
        // Start typing your C/C++ solution below
        // DO NOT write int main() function
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
        // Start typing your C/C++ solution below
        // DO NOT write int main() function
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

