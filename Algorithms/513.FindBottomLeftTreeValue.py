class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        cur_level, next_level, last_level = [], [], []
        cur_level.append(root)
        value = root.val
        while cur_level:
            node = cur_level.pop(0)
            if node.left:
                next_level.append(node.left);
            if node.right:
                next_level.append(node.right);
            if not cur_level:
                cur_level = next_level;
                if cur_level:
                    value = cur_level[0].val
                next_level = []
        return value
