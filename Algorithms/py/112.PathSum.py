class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a boolean
    def hasPathSum(self, root, sum):
        if not root: return False
        if not root.left and not root.right and root.val == sum:
            return True
        return (self.hasPathSum(root.left, sum - root.val) 
                or self.hasPathSum(root.right, sum - root.val))
