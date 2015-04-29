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
