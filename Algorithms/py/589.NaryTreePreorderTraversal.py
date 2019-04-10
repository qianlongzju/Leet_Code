"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        self.result = []
        self.preorder_iterative(root)
        return self.result
        
    def preorder_recursive(self, node):
        if node == None:
            return
        self.result.append(node.val)
        for child in node.children:
            self.preorder_recursive(child)
            
    def preorder_iterative(self, node):
        if node == None:
            return
        s = [node]
        while s:
            node = s.pop(-1)
            self.result.append(node.val)
            for child in node.children[::-1]:
                s.append(child)
