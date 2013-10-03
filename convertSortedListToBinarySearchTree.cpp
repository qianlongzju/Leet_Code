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
struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
/**
 * Definition for binary tree
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    TreeNode *sortedListToBST(ListNode *head) {
        // Start typing your C/C++ solution below
        // DO NOT write int main() function
        if (head == NULL) {
            return NULL;
        }
        if (head->next == NULL) {
            return new TreeNode(head->val);
        }
        ListNode* slow = head;
        ListNode* fast = head->next->next;
        while (fast != NULL && fast->next != NULL) {
            fast = fast->next->next;
            slow = slow->next;
        }
        TreeNode* root = new TreeNode(slow->next->val);
        root->right = sortedListToBST(slow->next->next);
        slow->next = NULL;
        root->left = sortedListToBST(head);
        return root;
    }
    //TreeNode *sortedListToBST(ListNode *head) {
    //    // Start typing your C/C++ solution below
    //    // DO NOT write int main() function
    //    int length = 0;
    //    ListNode* p = head;
    //    while (p != NULL) {
    //        length ++;
    //        p = p->next;
    //    }
    //    return sortedListToBST(head, 0, length-1);
    //}

    //TreeNode* sortedListToBST(ListNode* &list, int start, int end) {
    //    if (start > end) return NULL;
    //    // same as (start+end)/2, avoids overflow
    //    int mid = start + (end - start) / 2;
    //    TreeNode *leftChild = sortedListToBST(list, start, mid-1);
    //    TreeNode *parent = new TreeNode(list->val);
    //    parent->left = leftChild;
    //    list = list->next;
    //    parent->right = sortedListToBST(list, mid+1, end);
    //    return parent;
    //}       
};
int main() {
    Solution s;
    ListNode* head = new ListNode(1);
    s.sortedListToBST(head);

    return 0;
}

