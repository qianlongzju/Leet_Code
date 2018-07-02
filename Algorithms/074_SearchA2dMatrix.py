class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        low, high = 0, len(matrix) - 1
        while low < high:
            middle = low + (high - low)/2
            if matrix[middle][0] > target:
                high = middle - 1
            elif matrix[middle][0] < target:
                low = middle + 1
            else:
                return True
        if matrix[low][0] > target:
           row  = low - 1
           if row < 0:
               return False
        else:
            row = low
        low, high = 0, len(matrix[0])-1
        while low <= high:
            middle = low + (high - low)/2
            if matrix[row][middle] > target:
                high = middle - 1
            elif matrix[row][middle] < target:
                low = middle + 1
            else:
                return True
        return False
