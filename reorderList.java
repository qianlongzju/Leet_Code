import java.util.*;
/**
 * Definition for singly-linked list.
 * class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public void reorderList(ListNode head) {
        // IMPORTANT: Please reset any member data you declared, as
        // the same Solution instance will be reused for each test case.
        ListNode p = split(head);
        p = reverse(p);
        head = merge(head, p);
    }
    ListNode split(ListNode head) {
        if (head == null) 
            return head;
        ListNode slow = head;
        ListNode fast = head.next;
        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        }
        ListNode p = slow.next;
        slow.next = null;
        return p;
    }
    ListNode reverse(ListNode head) { 
        ListNode headptr = new ListNode(0);
        while (head != null) {
            ListNode tmp = head.next;
            head.next = headptr.next;
            headptr.next = head;
            head = tmp;
        }
        return headptr.next;
    }
    ListNode merge(ListNode p, ListNode q) {
        ListNode head = new ListNode(0);
        ListNode tmp = head;
        while (p != null && q != null) {
            tmp.next = p;
            p = p.next;
            tmp = tmp.next;
            tmp.next = q;
            q = q.next;
            tmp = tmp.next;
        }
        if (p != null) {
            tmp.next = p;
        }
        return head.next;
    }
}
