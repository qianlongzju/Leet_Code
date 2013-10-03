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
    public ListNode removeNthFromEnd(ListNode head, int n) {
        // Start typing your Java solution below
        // DO NOT write main() function
        int index = 0;
        ListNode p = head;
        ListNode del = null;
        while (p != null) {
            p = p.next;
            if (del != null) {
                del = del.next;
            }
            index ++;
            if (index == n+1) {
                del = head;
            }
        }
        if (index >= n+1) {
            del.next = del.next.next;
        }
        else {
            head = head.next;
        }
        return head;
    }
}
