class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        count = 0
        N = len(flowerbed)
        for i in range(N):
            if flowerbed[i] == 1:
                continue
            if (i == 0 or flowerbed[i-1] == 0) and (i+1 == N or flowerbed[i+1] == 0):
                flowerbed[i] = 1
                count += 1
        return count >= n
