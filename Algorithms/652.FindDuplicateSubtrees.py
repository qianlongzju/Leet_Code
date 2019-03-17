# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findDuplicateSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """
        def serialize(node):
            if node == None:
                return '#'
            return ",".join([serialize(node.left), serialize(node.right), str(node.val)])
        
        if root == None:
            return []
        d = {}
        q = [root]
        while q:
            node = q.pop(0)
            s = serialize(node)
            if s in d:
                d[s].append(node)
            else:
                d[s] = [node]
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        result = []
        for s, nodes in d.items():
            if len(nodes) > 1:
                result.append(nodes[0])
        return result

