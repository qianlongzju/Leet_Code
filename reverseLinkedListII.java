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
    public ListNode reverseBetween(ListNode head, int m, int n) {
        // Start typing your Java solution below
        // DO NOT write main() function
        if (m == n) {
            return head;
        }
        ListNode headptr = new ListNode(0);
        headptr.next = head;
        ListNode ins = headptr;
        ListNode p = head;
        for (int i=1; i < n; i++) {
            if (i < m) {
                ins = ins.next;
                p = p.next;
            }
            else {
                ListNode temp = p.next;
                p.next = temp.next;
                temp.next = ins.next;
                ins.next = temp;
            }
        }
        return headptr.next;
        
    }
}
