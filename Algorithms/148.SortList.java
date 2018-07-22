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
    public ListNode sortList(ListNode head) {
        int totalLength = genLength(head);
        if (totalLength == 0 || totalLength == 1) 
            return head;
        int leftLength = totalLength / 2;
        ListNode leftHead = head;
        ListNode rightHead = getRightHead(head, leftLength);
        leftHead = sortList(leftHead);
        rightHead = sortList(rightHead);
        return merge(leftHead, rightHead);
    }
    ListNode getRightHead(ListNode head, int leftLength) {
        ListNode rightHead = head;
        int i = 1;
        while (i < leftLength) {
            rightHead = rightHead.next;
            i ++;
        }
        ListNode p = rightHead.next;
        rightHead.next = null;
        rightHead = p;
        return rightHead;
    }
    ListNode merge(ListNode leftHead, ListNode rightHead) {
        ListNode headptr = new ListNode(0);
        ListNode p = headptr;
        while (leftHead != null && rightHead != null) {
            if (leftHead.val < rightHead.val) {
                p.next = leftHead;
                leftHead = leftHead.next;
            } else {
                p.next = rightHead;
                rightHead = rightHead.next;
            }
            p = p.next;
        }
        if (leftHead != null)
            p.next = leftHead;
        if (rightHead != null) 
            p.next = rightHead;
        return headptr.next;
    }
    int genLength(ListNode head) {
        ListNode p = head;
        int n = 0;
        while (p != null) {
            n++;
            p = p.next;
        }
        return n;
    }
}
