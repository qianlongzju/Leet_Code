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
    public ListNode deleteDuplicates(ListNode head) {
        // Start typing your Java solution below
        // DO NOT write main() function
        if (head == null) {
            return head;
        }
        ListNode p = head.next;
        ListNode previous = head;
        while (p != null) {
            if (p.val == previous.val) {
                previous.next = p.next;
            }
            else {
                previous = previous.next;
            }
            p = p.next;
        }
        return head;
    }
}
