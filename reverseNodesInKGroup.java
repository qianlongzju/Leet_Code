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
    public ListNode reverseKGroup(ListNode head, int k) {
        // Start typing your Java solution below
        // DO NOT write main() function
        if (k < 2 || head == null) {
            return head;
        }
        ListNode headptr = new ListNode(0);
        headptr.next = head;
        ListNode previous = headptr;
        ListNode p = head;
        ListNode pp = head;
        int count = 1;
        while (pp != null) {
            if (count == k) {
                pp = pp.next;
                while(p.next != pp) {
                    ListNode temp = p.next;
                    p.next = temp.next;
                    temp.next = previous.next;
                    previous.next = temp;
                }
                previous = p;
                p = p.next;
                count = 1;
            }
            else {
                pp = pp.next;
                count ++;
            }
        }
        return headptr.next;
    }
}
