class Solution:
    # @param root, a tree node
    # @return an integer
    def maxDepth(self, root):
        if not root:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        self.max_d = None
        self._dfs(root, 1)
        return self.max_d
    def _dfs(self, node, depth):
        if node.left == None and node.right == None:
            if self.max_d == None:
                self.max_d = depth
            else:
                self.max_d = max(self.max_d, depth)
        if node.left:
            self._dfs(node.left, depth + 1)
        if node.right:
            self._dfs(node.right, depth + 1)

    def maxDepth(self, root):
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
                    max_d = level
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return max_d

