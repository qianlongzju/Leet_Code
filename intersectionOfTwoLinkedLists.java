/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
    	int lenA = lengthOfList(headA);
    	int lenB = lengthOfList(headB);
    	if (lenA > lenB) {
    		int diff = lenA - lenB;
    		while (diff > 0) {
    			headA = headA.next;
    			diff --;
    		}
    	} else {
    		int diff = lenB - lenA;
    		while (diff > 0) {
    			headB = headB.next;
    			diff --;
    		}
    	}
    	while (headA != null && headB != null) {
    		if (headA.val == headB.val) 
    			return headA;
    		headA = headA.next;
    		headB = headB.next;
    	}
    	return null;       
    }
    private int lengthOfList(ListNode head) {
    	int length = 0;
    	while (head != null) {
    		length ++;
    		head = head.next;
    	}
    	return length;
    }
}