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
    def construct(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: Node
        """
        def valid(i, j, m, n):
            vals = set()
            for x in range(i, m+1):
                for y in range(j, n+1):
                    vals.add(grid[x][y])
                    if len(vals) > 1:
                        return -1
            return vals.pop()
        
        def help(i, j, m, n):
            v = valid(i, j, m, n)
            if v == 0:
                return Node(False, True, None, None, None, None)
            elif v == 1:
                return Node(True, True, None, None, None, None)
            else:
                mid_x, mid_y = (m+i)/2, (n+j)/2
                topLeft = help(i, j, mid_x, mid_y)
                topRight = help(i, mid_y+1, mid_x, n)
                bottomLeft = help(mid_x+1, j, m, mid_y)
                bottomRight = help(mid_x+1, mid_y+1, m, n)
                return Node("*", False, topLeft, topRight, bottomLeft, bottomRight)
            
        N = len(grid)
        return help(0, 0, N-1, N-1)
