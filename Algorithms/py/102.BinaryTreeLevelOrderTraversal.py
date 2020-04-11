class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def levelOrder(self, root):
        result = []
        if not root: return result
        queue = [root]
        next_queue = []
        values = []
        while queue:
            node = queue.pop(0)
            values.append(node.val)
            if node.left: next_queue.append(node.left)
            if node.right: next_queue.append(node.right)
            if not queue:
                result.append(values[:])
                values = []
                queue = next_queue
                next_queue = []
        return result

    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result = []
        def _dfs(node, level):
            if not node:
                return
            if len(result) < level + 1:
                result.append([])
            result[level].append(node.val)
            if node.left:
                _dfs(node.left, level + 1)
            if node.right:
                _dfs(node.right, level + 1)
        _dfs(root, 0)
        return result
