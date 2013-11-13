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
    public ListNode mergeKLists(ArrayList<ListNode> lists) {
        // Start typing your Java solution below
        // DO NOT write main() function
        if (lists.size() == 0) {
            return null;
        }
        if (lists.size() == 1) {
            return lists.get(0);
        }
        ListNode p = lists.get(0);
        for (int i=1; i < lists.size(); ++i) {
            p = mergeTwoLists(p, lists.get(i));
        }
        return p;
    }
    public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
        // Start typing your Java solution below
        // DO NOT write main() function
        ListNode head = null;
        ListNode p = null;
        while (l1 != null && l2 != null) {
            if (l1.val < l2.val) {
                if (head == null) {
                    head = l1;
                    p = l1;
                }
                else {
                    p.next = l1;
                    p = l1;
                }
                l1 = l1.next;
            }
            else {
                if (head == null) {
                    head = l2;
                    p = l2;
                }
                else {
                    p.next = l2;
                    p = l2;
                }
                l2 = l2.next;
            }
        }
        if (l1 != null) {
            if (head == null) {
                head = l1;
            }
            else {
                p.next = l1;
            }
        }
        if (l2 != null) {
            if (head == null) {
                head = l2;
            }
            else {
                p.next = l2;
            }
        }
        return head;
    }
}
