class Solution:
    # @param {TreeNode} root
    # @return {integer[]}
    def preorderTraversal_1(self, root):
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
    
    def preorderTraversal(self, root):
        q = [root]
        v = []
        while q:
            node = q.pop(-1)
            if node == None:
                continue
            v.append(node.val)
            if node.right:
                q.append(node.right)
            if node.left:
                q.append(node.left)
        return v
