# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isCousins(self, root, x, y):
        """
        :type root: TreeNode
        :type x: int
        :type y: int
        :rtype: bool
        """
        q, next_q = [root], []
        parent = {}
        current_value = set()
        while q:
            node = q.pop(0)
            current_value.add(node.val)
            if node.left:
                next_q.append(node.left)
                parent[node.left.val] = node
            if node.right:
                next_q.append(node.right)
                parent[node.right.val] = node
            if q == []:
                if x in current_value:
                    if y in current_value:
                        return parent[x] != parent[y]
                    else:
                        return False
                current_value = set()
                q, next_q = next_q, []
        return False
        
