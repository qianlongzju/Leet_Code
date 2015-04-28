class Solution:
    # @param root, a tree node
    # @return a boolean
    def isSymmetric(self, root):
        if not root: return True
        return self.isSymmetricHelper(root.left, root.right)
        
    def isSymmetricHelper(self, left, right):
        if not left and right:
            return False
        if left and not right:
            return False
        if not left and not right:
            return True
        if left.val != right.val:
            return False
        return self.isSymmetricHelper(left.left, right.right) and self.isSymmetricHelper(left.right, right.left)
