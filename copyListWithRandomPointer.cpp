#include <iostream>
#include <string>
#include <sstream>
#include <stack>
#include <vector>
#include <queue>
#include <set>
#include <algorithm>
#include <limits.h>
#include <stdlib.h>
#include <math.h>
using namespace std;
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};
struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};
void printTree(TreeNode* root) {
    if (root == NULL) {
        return;
    }
    queue<TreeNode *> treeNodeQueue;
    queue<char> numQueue;
    treeNodeQueue.push(root);
    while (!treeNodeQueue.empty()) {
        TreeNode* tmp = treeNodeQueue.front();
        treeNodeQueue.pop();
        if (tmp != NULL) {
            numQueue.push(tmp->val + '0');
        } else {
            numQueue.push('#');
            continue;
        }
        if (tmp->left != NULL) {
            treeNodeQueue.push(tmp->left);
        } else {
            treeNodeQueue.push(NULL);
        }
        if (tmp->right != NULL) {
            treeNodeQueue.push(tmp->right);
        } else {
            treeNodeQueue.push(NULL);
        }
    }
    while (!numQueue.empty()) {
        char c = numQueue.front();
        cout << c;
        numQueue.pop();
    }
}
struct RandomListNode {
    int label;
    RandomListNode *next, *random;
    RandomListNode(int x) : label(x), next(NULL), random(NULL) {}
};
/**
 * Definition for singly-linked list with a random pointer.
 * struct RandomListNode {
 *     int label;
 *     RandomListNode *next, *random;
 *     RandomListNode(int x) : label(x), next(NULL), random(NULL) {}
 * };
 */
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

