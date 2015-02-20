import java.util.*;
public class Solution {
    public RandomListNode copyRandomList(RandomListNode head) {
        Clone(head);
        CopyRandomPointer(head);
        return restore(head);
    }
    void Clone(RandomListNode head) {
        RandomListNode pNode = head;
        while (pNode != null) {
            RandomListNode clonedNode = new RandomListNode(pNode.label);
            clonedNode.next = pNode.next;
            pNode.next = clonedNode;
            pNode = clonedNode.next;
        }
    }
    void CopyRandomPointer(RandomListNode head) {
        RandomListNode pNode = head;
        while (pNode != null) {
            RandomListNode clonedNode = pNode.next;
            if (pNode.random != null) {
                clonedNode.random = pNode.random.next;
            }
            pNode = clonedNode.next;
        }
    }
    RandomListNode restore(RandomListNode head) {
        RandomListNode pNode = head;
        RandomListNode pClonedHead = null;
        RandomListNode pClonedNode = null;
        if (pNode != null) {
            pClonedHead = pNode.next;
            pClonedNode = pNode.next;
            pNode.next = pClonedNode.next;
            pNode = pNode.next; 
        }
        while (pNode != null) {
            pClonedNode.next = pNode.next;
            pClonedNode = pClonedNode.next;
            pNode.next = pClonedNode.next;
            pNode = pNode.next;
        }
        return pClonedHead;
    }
}
