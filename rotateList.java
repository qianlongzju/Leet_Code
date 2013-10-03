/**
 * Definition for singly-linned list.
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
    public ListNode rotateRight(ListNode head, int n) {
        // Start typing your Java solution below
        // DO NOT write main() function
        if (head == null) {
            return head;
        }
        ListNode p = head;
        int count = 0;
        while (p != null) {
            p = p.next;
            count ++;
        }
        n = n % count;
        if (n == 0) {
            return head;
        }
        p = head;
        ListNode q = null;
        ListNode r = null;
        count = 0;
        while (p != null) {
            r = p;
            p = p.next;
            count ++;
            if (q != null) {
                q = q.next;
            }
            if (count == n+1) {
                q = head;
            }
        }
        r.next = head;
        head = q.next;
        q.next = null;
        return head;
    }
}
