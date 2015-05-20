class Solution:
    # @param {TreeNode} root
    # @return {integer[]}
    def postorderTraversal(self, root):
        v = []
        if not root: return v
        stack, prevNode = [root], None
        while stack:
            currNode = stack[-1]
            if (not prevNode or prevNode.left == currNode or
                    prevNode.right == currNode):
                if currNode.left:
                    stack.append(currNode.left)
                elif currNode.right:
                    stack.append(currNode.right)
            elif currNode.left == prevNode:
                if currNode.right:
                    stack.append(currNode.right)
            else:
                v.append(currNode.val)
                stack.pop()
            prevNode = currNode
        return v
