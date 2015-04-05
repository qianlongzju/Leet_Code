class Solution:
    # @param num, a list of integers
    # @return a tree node
    def sortedArrayToBST(self, num):
       return self.sortedSubArrayToBST(num, 0, len(num)-1)

    def sortedSubArrayToBST(self, num, start, end):
        if not num: return None
        mid = (start + end) / 2
        root = TreeNode(num[mid])
        root.left = self.sortedSubArrayToBST(num, start, mid-1)
        root.right = self.sortedSubArrayToBST(num, mid+1, end)
        return root
