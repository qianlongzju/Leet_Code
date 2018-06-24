class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i, j = 0, len(height)-1
        max_area = 0
        while i < j:
            if height[i] < height[j]:
                area = (j-i) * height[i]
                i += 1
            else:
                area = (j-i) * height[j]
                j -= 1
            max_area = max(area, max_area)
        return max_area
