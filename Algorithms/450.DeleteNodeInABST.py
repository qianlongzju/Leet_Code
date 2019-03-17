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
            if key == node.val:
                if node.left == None and node.right == None:
                    if parent == None:
                        return None
                    elif parent.left == node:
                        parent.left = None
                    else:
                        parent.right = None
                    return root
                elif node.left == None and node.right != None:
                    if parent == None:
                        return node.right
                    if parent.left == node:
                        parent.left = node.right
                    else:
                        parent.right = node.right
                    return root
                elif node.left != None and node.right == None:
                    if parent == None:
                        return node.left
                    if parent.left == node:
                        parent.left = node.left
                    else:
                        parent.right = node.left
                    return root
                else:
                    parent, x_node = node, node.right
                    while x_node.left:
                        parent = x_node
                        x_node = x_node.left
                    node.val, x_node.val = x_node.val, node.val
                    node = x_node
            elif key > node.val:
                parent, node = node, node.right
            else:
                parent, node = node, node.left
        return root
