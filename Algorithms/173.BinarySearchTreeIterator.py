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
