public class Solution {
    public ListNode deleteDuplicates(ListNode head) {
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
