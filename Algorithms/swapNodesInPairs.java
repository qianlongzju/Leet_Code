public class Solution {
    public ListNode swapPairs(ListNode head) {
        if (head == null || head.next == null) {
            return head;
        }
        ListNode p = head;
        head = head.next;
        p.next = head.next;
        head.next = p;
        ListNode q = p.next;
        while (q != null && q.next != null) {
            ListNode r = q.next;
            q.next = q.next.next;
            r.next = q;
            p.next = r;
            p = p.next.next;
            q = q.next;
        }
        return head;
    }
}
