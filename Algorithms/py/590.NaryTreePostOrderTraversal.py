"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        self.result = []
        self.postorder_iterative(root)
        return self.result
    
    def postorder_recursive(self, node):
        if node == None:
            return
        for child in node.children:
            self.postorder_recursive(child)
        self.result.append(node.val)
        
    def postorder_iterative(self, node):
        if node == None:
            return
        s = [node]
        pre = None
        while s:
            node = s[-1]
            if node.children == [] or node.children[-1] == pre:
                self.result.append(node.val)
                pre = s.pop(-1)
            else:
                s.extend(node.children[::-1])
