import java.util.*;
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
    public ListNode partition(ListNode head, int x) {
        // Note: The Solution object is instantiated only once and is reused by each test case.
        ListNode leftheadptr = new ListNode(0);
        ListNode rightheadptr = new ListNode(0);
        ListNode left = new ListNode(0);
        ListNode right = new ListNode(0);
        leftheadptr = left;
        rightheadptr = right;
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
