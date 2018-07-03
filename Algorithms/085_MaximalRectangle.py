class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        m = len(matrix)
        if m == 0:
            return 0
        n = len(matrix[0])
        heights = [[0 for i in range(n)] for j in range(m)]
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '0':
                    continue
                if i == 0:
                    heights[i][j] = 1
                else: 
                    heights[i][j] = heights[i-1][j] + 1
        maxArea = 0
        for i in range(m):
            maxArea = max(maxArea, self.largestRectangleArea(heights[i]))
        return maxArea

    def largestRectangleArea(self, height):
        if len(height) < 1:
            return 0
        heights, indexes = [height[0]], [0]
        largestArea = height[0]
        i = 1
        while i < len(height):
            if height[i] >= heights[-1]:
                heights.append(height[i])
                indexes.append(i)
            else:
                h, j = 0, 0
                while heights and height[i] < heights[-1]:
                    h = heights[-1]
                    j = indexes[-1]
                    largestArea = max(largestArea, h * (i - j))
                    heights.pop(-1)
                    indexes.pop(-1)
                heights.append(height[i])
                indexes.append(j)
            i += 1
        while heights:
            if heights[-1] * (i - indexes[-1]) > largestArea:
                largestArea = heights[-1] * (i - indexes[-1])
            heights.pop(-1)
            indexes.pop(-1)
        return largestArea
