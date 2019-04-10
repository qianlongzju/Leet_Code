public class Solution {
    public ListNode deleteDuplicates(ListNode head) {
        if (head == null) {
            return head;
        }
        ListNode headptr = new ListNode(head.val-1);
        headptr.next = head;
        ListNode previous = headptr;
        ListNode p = head;
        boolean remove = false;
        while (p != null) {
            while (p != null && p.next != null && p.val == p.next.val) {
                remove = true;
                p = p.next;
            }
            if (remove) {
                previous.next = p.next;
                p = p.next;
                remove = false;
            }
            else {
                p = p.next;
                previous = previous.next;
            }
        }
        return headptr.next;
    }
}
