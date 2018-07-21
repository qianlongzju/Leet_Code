# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        if not root:
            return result
        cur_level, next_level = [], []
        cur_level.append(root)
        maximum = root.val
        while cur_level:
            node = cur_level.pop(0)
            maximum = max(maximum, node.val)
            if node.left:
                next_level.append(node.left)
            if node.right:
                next_level.append(node.right)
            if not cur_level:
                result.append(maximum)
                if not next_level:
                    break;
                cur_level = next_level
                next_level = []
                maximum = cur_level[0].val
        return result
