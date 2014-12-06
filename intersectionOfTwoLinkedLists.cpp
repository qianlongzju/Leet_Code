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
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
        int lenA = getLengthOfList(headA);
        int lenB = getLengthOfList(headB);
        if (lenA > lenB) {
        	int diff = lenA - lenB;
        	while (diff > 0) {
        		headA = headA->next;
        		diff --;
        	}
        } else {
        	int diff = lenB - lenA;
        	while (diff > 0) {
        		headB = headB->next;
        		diff --;
        	}
        }
        while (headA != NULL && headB != NULL) {
        	if (headA->val == headB->val) {
        		return headA;
        	}
        	headA = headA->next;
        	headB = headB->next;
        }
        return NULL;
    }
private:
	int getLengthOfList(ListNode *head) {
		int length = 0;
		while (head != NULL) {
			length ++;
			head = head->next;
		}
        return length;
	}
};


