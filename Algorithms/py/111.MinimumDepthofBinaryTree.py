class Solution:
    # @param root, a tree node
    # @return an integer
    def minDepth(self, root):
        if not root: return 0
        left = self.minDepth(root.left)
        right = self.minDepth(root.right)
        if not left: return 1 + right
        if not right: return 1 + left
        return 1 + min(left, right)

    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        return self._bfs(root)

    def _bfs(self, root):
        q = [root]
        level = 0
        max_d = None
        while q:
            size = len(q)
            level += 1
            for _ in range(size):
                node = q.pop(0)
                if node.left == None and node.right == None:
                    return level
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        self.min_d = None
        self._dfs(root, 1)
        return self.min_d

    def _dfs(self, node, depth):
        if node.left == None and node.right == None:
            if self.min_d == None:
                self.min_d = depth
            else:
                self.min_d = min(self.min_d, depth)
        if node.left:
            self._dfs(node.left, depth + 1)
        if node.right:
            self._dfs(node.right, depth + 1)
