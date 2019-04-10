# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None:
            return []
        self.vals = []
        self.inorder(root)
        count, max_count = 1, 0
        result = []
        #print self.vals
        for i in range(1, len(self.vals)):
            if self.vals[i] == self.vals[i-1]:
                count += 1
            else:
                if count > max_count:
                    max_count = count
                    result = [self.vals[i-1]]
                elif count == max_count:
                    result.append(self.vals[i-1])
                count = 1
        else:
                if count > max_count:
                    max_count = count
                    result = [self.vals[-1]]
                elif count == max_count:
                    result.append(self.vals[-1])
        return result
        
    def inorder(self, node):
        if node == None:
            return
        self.inorder(node.left)
        self.vals.append(node.val)
        self.inorder(node.right)
