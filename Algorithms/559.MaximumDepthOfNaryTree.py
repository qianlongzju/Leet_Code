"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        self.max_depth = 0
        self.maxDepthHelper(root, 0)
        return self.max_depth
    
    def maxDepthHelper(self, root, depth):
        if root:
            depth += 1
        else:
            return
        if root.children:
            for child in root.children:
                self.maxDepthHelper(child, depth)
        else:
            self.max_depth = max(self.max_depth, depth)
