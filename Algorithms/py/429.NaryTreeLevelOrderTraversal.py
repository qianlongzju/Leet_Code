"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        result = []
        if root == None:
            return result
        q, next_q = [root], []
        vals = []
        while q:
            node = q.pop(0)
            vals.append(node.val)
            for child in node.children:
                next_q.append(child)
            if q == []:
                q, next_q = next_q, []
                result.append(vals[:])
                vals = []
        return result
