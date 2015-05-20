class Solution:
    # @param {TreeNode} root
    # @return {integer[]}
    def preorderTraversal(self, root):
        v, stack, p = [], [], root
        while stack or p:
            if p:
                v.append(p.val)
                if p.right:
                    stack.append(p.right)
                p = p.left
            else:
                p = stack.pop()
        return v
