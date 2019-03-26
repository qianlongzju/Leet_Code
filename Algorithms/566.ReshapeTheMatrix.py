class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        row, col = len(nums), len(nums[0])
        if row * col != r * c:
            return nums
        result = [[0] * c for i in range(r)]
        for i in range(row):
            for j in range(col):
                index = i * col + j
                rr, cc = index / c, index % c
                result[rr][cc] = nums[i][j]
        return result
