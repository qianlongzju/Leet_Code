import java.util.*;
public class Solution {
    public ListNode partition(ListNode head, int x) {
        ListNode leftheadptr = new ListNode(0);
        ListNode rightheadptr = new ListNode(0);
        ListNode left = leftheadptr;
        ListNode right = rightheadptr;
        while (head != null) {
            if (head.val < x) {
                left.next = head;
                left = left.next;
            } else {
                right.next = head;
                right = right.next;
            }
            head = head.next;
        }
        left.next = rightheadptr.next;
        right.next = null;
        return leftheadptr.next;
    }
}
