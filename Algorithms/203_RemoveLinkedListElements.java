/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode removeElements(ListNode head, int val) {
        ListNode dummyHead = new ListNode(0);
        dummyHead.next = head;
        ListNode previous = dummyHead;
        ListNode current = head;
        while(current != null) {
            if (current.val == val) {
                previous.next = current.next;
                current = current.next;
            } else {
                previous = previous.next;
                current = current.next;
            }
        }
        return dummyHead.next;
    }
}
