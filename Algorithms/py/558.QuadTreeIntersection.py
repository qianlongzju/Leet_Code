"""
# Definition for a QuadTree node.
class Node(object):
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""
class Solution(object):
    def intersect(self, quadTree1, quadTree2):
        """
        :type quadTree1: Node
        :type quadTree2: Node
        :rtype: Node
        """
        if quadTree1.isLeaf and quadTree2.isLeaf:
            return Node(quadTree1.val or quadTree2.val, True, None, None, None, None)
        elif quadTree1.isLeaf and not quadTree2.isLeaf:
            if quadTree1.val == True:
                return quadTree1
            else:
                return quadTree2
        elif not quadTree1.isLeaf and quadTree2.isLeaf:
            return self.intersect(quadTree2, quadTree1)
        else:
            topLeft = self.intersect(quadTree1.topLeft, quadTree2.topLeft)
            topRight = self.intersect(quadTree1.topRight, quadTree2.topRight)
            bottomLeft = self.intersect(quadTree1.bottomLeft, quadTree2.bottomLeft)
            bottomRight = self.intersect(quadTree1.bottomRight, quadTree2.bottomRight)
            if topLeft.isLeaf and topRight.isLeaf and bottomLeft.isLeaf and bottomRight.isLeaf and topLeft.val == topRight.val == bottomLeft.val == bottomRight.val:
                return topLeft
            return Node("*", False, topLeft, topRight, bottomLeft, bottomRight)
