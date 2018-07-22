class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        return self.sortedSubArrayToBST(nums, 0, len(nums)-1)

    def sortedSubArrayToBST(self, nums, start, end):
        if start > end: return None
        mid = (start + end) / 2
        root = TreeNode(nums[mid])
        root.left = self.sortedSubArrayToBST(nums, start, mid-1)
        root.right = self.sortedSubArrayToBST(nums, mid+1, end)
        return root
