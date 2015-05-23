class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None
class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if not root: return
        while root:
            start = self.nextLevelFirstNode(root)
            curr_node = start
            while curr_node:
                root, next_node = self.nextLevelNextNode(root, curr_node)
                curr_node.next = next_node
                curr_node = next_node
            root = start

    def nextLevelFirstNode(self, root):
        if not root: return None
        if root.left: return root.left
        return self.nextLevelNextNode(root, root.left)[1]

    def nextLevelNextNode(self, root, curr_node):
        if root.left == curr_node and root.right:
            return root, root.right
        while root.next:
            root = root.next
            if root.left: return root, root.left
            if root.right: return root, root.right
        return root, None

A = TreeLinkNode(1)
B = TreeLinkNode(2)
C = TreeLinkNode(3)
D = TreeLinkNode(4)
E = TreeLinkNode(5)
A.left, A.right = B, C
B.left = D
C.right = E
S = Solution()
S.connect(A)
