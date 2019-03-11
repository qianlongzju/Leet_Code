class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        for i in range(len(A)):
            j, k = 0, len(A[0]) - 1
            while j < k:
                A[i][j], A[i][k] = 1-A[i][k], 1-A[i][j]
                j += 1
                k -= 1
            if j == k:
                A[i][j] = 1-A[i][j]
        return A
