class Solution:
    # @param root, a tree node
    # @return an integer
    def sumNumbers(self, root):
        self.total = 0
        self.sumNumbersHelper(root, 0)
        return self.total
        
    def sumNumbersHelper(self, root, s):
        if not root: return
        s = s * 10 + root.val
        if not root.left and not root.right:
            self.total += s
        if root.left:
            self.sumNumbersHelper(root.left, s)
        if root.right:
            self.sumNumbersHelper(root.right, s)
