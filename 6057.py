# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def averageOfSubtree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        return self.sumOfSubtree(root)[2]
        
    
    def sumOfSubtree(self, root):
        if not root:
            return 0, 0, 0
        left_sum, left_num, left_cnt = self.sumOfSubtree(root.left)
        right_sum, right_num, right_cnt = self.sumOfSubtree(root.right)
        total_sum = left_sum + right_sum + root.val
        total_num = left_num + right_num + 1
        if total_sum // total_num == root.val:
            cnt = 1
        else:
            cnt = 0
        return total_sum, total_num, left_cnt + right_cnt + cnt
