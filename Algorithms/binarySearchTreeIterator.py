# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BSTIterator:
    # @param root, a binary search tree's root node
    def __init__(self, root):
        self.path = []
        while root:
            self.path.append(root)
            root = root.left

    # @return a boolean, whether we have a next smallest number
    def hasNext(self):
        return len(self.path) != 0
        

    # @return an integer, the next smallest number
    def next(self):
        #print 'path:', self.path[-1].val
        result = self.path[-1]
        self.path.pop()
        temp = result.right
        while temp:
            self.path.append(temp)
            temp = temp.left
        return result.val
# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())
root = TreeNode(1)
i, v = BSTIterator(root), []
while i.hasNext(): v.append(i.next())
print v
