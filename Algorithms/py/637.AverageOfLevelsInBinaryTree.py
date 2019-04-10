# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        if root == None:
            return []
        q, next_q = [root], []
        cur_values = []
        result = []
        while q:
            node = q.pop(0)
            cur_values.append(node.val)
            if node.left:
                next_q.append(node.left)
            if node.right:
                next_q.append(node.right)
            if q == []:
                q, next_q = next_q, []
                result.append(sum(cur_values) * 1.0 / len(cur_values))
                cur_values = []
        return result
