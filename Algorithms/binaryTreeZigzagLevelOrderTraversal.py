class Solution:
    # @param {TreeNode} root
    # @return {integer[][]}
    def zigzagLevelOrder(self, root):
        result = []
        if not root: return result
        queue, next_queue, values, flag = [root], [], [], True
        while queue:
            node = queue.pop(0)
            values.append(node.val)
            if node.left: next_queue.append(node.left)
            if node.right: next_queue.append(node.right)
            if not queue:
                if flag:
                    result.append(values[:])
                else:
                    result.append(values[::-1])
                values, queue, next_queue, flag = [], next_queue, [], not flag
        return result
