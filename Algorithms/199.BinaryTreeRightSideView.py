class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        if not root:
            return result
        result.append(root.val)
        cur_level, next_level = [], []
        cur_level.append(root)
        while cur_level:
            node = cur_level.pop(0)
            if node.left:
                next_level.append(node.left)
            if node.right:
                next_level.append(node.right)
            if not cur_level:
                cur_level = next_level
                next_level = []
                if cur_level:
                    result.append(cur_level[-1].val)
        return result
