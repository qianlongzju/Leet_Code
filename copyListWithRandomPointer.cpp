#include "leetcode.h"
class Solution {
public:
    RandomListNode *copyRandomList(RandomListNode *head) {
        // Note: The Solution object is instantiated only once and is reused by each test case.
        Clone(head);
        CopyRandomPointer(head);
        return restore(head);
    }
    void Clone(RandomListNode *head) {
        RandomListNode *pNode = head;
        while (pNode != NULL) {
            RandomListNode *clonedNode = new RandomListNode(pNode->label);
            clonedNode->next = pNode->next;
            pNode->next = clonedNode;
            pNode = clonedNode->next;
        }
    }
    void CopyRandomPointer(RandomListNode *head) {
        RandomListNode *pNode = head;
        while (pNode != NULL) {
            RandomListNode *clonedNode = pNode->next;
            if (pNode->random != NULL) {
                clonedNode->random = pNode->random->next;
            }
            pNode = clonedNode->next;
        }
    }
    RandomListNode *restore(RandomListNode *head) {
        RandomListNode *pNode = head;
        RandomListNode *pClonedHead = NULL;
        RandomListNode *pClonedNode = NULL;
        if (pNode != NULL) {
            pClonedHead = pNode->next;
            pClonedNode = pNode->next;
            pNode->next = pClonedNode->next;
            pNode = pNode->next; 
        }
        while (pNode != NULL) {
            pClonedNode->next = pNode->next;
            pClonedNode = pClonedNode->next;
            pNode->next = pClonedNode->next;
            pNode = pNode->next;
        }
        return pClonedHead;
    }
};
int main() {
    Solution s;
    RandomListNode *a = new RandomListNode(-1);
    RandomListNode *b = new RandomListNode(1);
    a->next = b;
    s.copyRandomList(a);
    return 0;
}

