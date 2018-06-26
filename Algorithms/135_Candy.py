class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        n = len(ratings)
        if n == 1:
            return 1
        result, leftToRight, rightToLeft = [0] * n, [0] * n, [0] * n
        # 1:bigger  -1:smaller 0:equal
        leftToRight[0] = 0
        for i in range(1, n):
            if ratings[i] > ratings[i-1]:
                leftToRight[i] = 1
            elif ratings[i] < ratings[i-1]:
                leftToRight[i] = -1
            else:
                leftToRight[i] = 0
        rightToLeft[n-1] = 0
        for i in range(n-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                rightToLeft[i] = 1
            elif ratings[i] < ratings[i+1]:
                rightToLeft[i] = -1
            else:
                rightToLeft[i] = 0
        for i in range(n):
            if leftToRight[i] <= 0 and rightToLeft[i] <= 0:
                result[i] = 1
        for i in range(n):
            if result[i] == 1:
                i += 1
                while i < n and ratings[i] > ratings[i-1]:
                    result[i] = result[i-1] + 1
                    i += 1
                i -= 1
        for i in range(n-1, -1, -1):
            if result[i] == 1:
                i -= 1
                while i >=0 and ratings[i] > ratings[i+1]:
                    result[i] = result[i+1] + 1
                    i -= 1
                if i >= 0 and i+2 <= n-1 and ratings[i] < ratings[i+1]:
                    result[i+1] = max(result[i], result[i+2]) + 1
                i += 1
        return sum(result)
