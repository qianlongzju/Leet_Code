class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        if len(heights) < 1:
            return 0
        h, indexes = [heights[0]], [0]
        largestArea = heights[0]
        i = 1
        while i < len(heights):
            if heights[i] >= h[-1]:
                h.append(heights[i])
                indexes.append(i)
            else:
                j = 0
                while h and heights[i] < h[-1]:
                    j = indexes[-1]
                    largestArea = max(h[-1] * (i - j), largestArea)
                    h.pop(-1)
                    indexes.pop(-1)
                h.append(heights[i])
                indexes.append(j)
            i += 1
        while h:
            largestArea = max(h[-1] * (i - indexes[-1]), largestArea)
            h.pop(-1)
            indexes.pop(-1)
        return largestArea
