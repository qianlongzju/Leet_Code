# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        node, parent = root, None
        while node:
            if key > node.val:
                parent, node = node, node.right
            elif key < node.val:
                parent, node = node, node.left
            else:
                if node.left != None and node.right != None:
                    min_parent, min_node = node, node.right
                    while min_node.left:
                        min_parent, min_node = min_node, min_node.left
                    node.val, min_node.val = min_node.val, node.val
                    parent, node = min_parent, min_node

                child = None
                if node.left:
                    child = node.left
                elif node.right:
                    child = node.right
                if parent == None:
                    return child
                elif parent.left == node:
                    parent.left = child
                else:
                    parent.right = child
                return root
        return root
