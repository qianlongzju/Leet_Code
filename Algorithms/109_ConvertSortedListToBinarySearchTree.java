import java.util.*;
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; next = null; }
 * }
 */
/**
 * Definition for binary tree
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class Solution {
    private ListNode list;
    TreeNode sortedListToBST(ListNode head) {
        int length = 0;
        ListNode p = head;
        while (p != null) {
            length ++;
            p = p.next;
        }
        this.list = head;
        return sortedListToBST(0, length-1);
    }

    TreeNode sortedListToBST(int start, int end) {
        if (start > end) return null;
        int mid = start + (end - start) / 2;
        TreeNode leftChild = sortedListToBST(start, mid-1);
        TreeNode parent = new TreeNode(list.val);
        parent.left = leftChild;
        this.list = this.list.next;
        parent.right = sortedListToBST(mid+1, end);
        return parent;
    }       
    /*
    TreeNode sortedListToBST(ListNode head) {
        int length = 0;
        ListNode p = head;
        while (p != null) {
            length ++;
            p = p.next;
        }
        p = new ListNode(0);
        p.next = head;
        return sortedListToBST(p, 0, length-1);
    }

    TreeNode sortedListToBST(ListNode list, int start, int end) {
        if (start > end) return null;
        int mid = start + (end - start) / 2;
        TreeNode leftChild = sortedListToBST(list, start, mid-1);
        TreeNode parent = new TreeNode(list.next.val);
        parent.left = leftChild;
        list.next = list.next.next;
        parent.right = sortedListToBST(list, mid+1, end);
        return parent;
    }       
    */
    /*
    public TreeNode sortedListToBST(ListNode head) {
        if (head == null) {
            return null;
        }
        if (head.next == null) {
            return new TreeNode(head.val);
        }
        ListNode slow = head;
        ListNode fast = head.next.next;
        while (fast != null && fast.next != null) {
            fast = fast.next.next;
            slow = slow.next;
        }
        TreeNode root = new TreeNode(slow.next.val);
        root.right = sortedListToBST(slow.next.next);
        slow.next = null;
        root.left = sortedListToBST(head);
        return root;
    }
    */
}
