class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a list of lists of integers
    def pathSum(self, root, sum):
        self.result = []
        self.path = []
        self.pathSumHelper(root, sum)
        return self.result
    def pathSumHelper(self, root, sum):
        if not root: return
        self.path.append(root.val)
        if not root.left and not root.right and root.val == sum:
            self.result.append(self.path[:])
            self.path.pop()
            return
        self.pathSumHelper(root.left, sum - root.val)
        self.pathSumHelper(root.right, sum - root.val)
        self.path.pop()

