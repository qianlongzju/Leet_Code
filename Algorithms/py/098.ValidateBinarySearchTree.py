class Solution:
    # @param root, a tree node
    # @return a boolean
    def isValidBST(self, root):
        return self.validBST(root, None, None)

    def validBST(self, root, Min, Max):
        if not root:
            return True
        if Min != None and Min >= root.val:
            return False
        if Max != None and Max <= root.val:
            return False
        return (self.validBST(root.left, Min, root.val) 
            and self.validBST(root.right, root.val, Max))

    # inorder
    def isValidBST(self, root):
        self.prev = None
        return self.helper(root)

    def helper(self, root):
        if root is None:
            return True
        if not self.helper(root.left):
            return False
        if self.prev and self.prev.val >= root.val:
            return False
        self.prev = root
        return self.helper(root.right)

