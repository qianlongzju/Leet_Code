class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        self.pre, self.node1, self.node2 = None, None, None
        self.recoverTreeRecursive(root)
        self.node1.val, self.node2.val = self.node2.val, self.node1.val

    def recoverTreeRecursive(self, root):
        if not root:
            return
        self.recoverTreeRecursive(root.left)
        if self.pre and root.val < self.pre.val:
            if not self.node1:
                self.node1 = self.pre
                self.node2 = root
            else:
                self.node2 = root
        self.pre = root
        self.recoverTreeRecursive(root.right)
