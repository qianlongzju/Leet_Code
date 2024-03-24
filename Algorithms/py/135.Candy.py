class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        if n == 1:
            return 1
        result = [0] * n
        if ratings[0] <= ratings[1]:
            result[0] = 1
        if ratings[-1] <= ratings[-2]:
            result[-1] = 1
        for i in range(1, n-1):
            if ratings[i] <= ratings[i-1] and ratings[i] <= ratings[i+1]:
                result[i] = 1
        i = 0
        while i < n:
            if result[i] == 1:
                i += 1
                while i < n and ratings[i] > ratings[i-1]:
                    result[i] = result[i-1] + 1
                    i += 1
                i -= 1
            i += 1
        i = n-1
        while i >= 0:
            if result[i] == 1:
                i -= 1
                while i >= 0 and ratings[i] > ratings[i+1]:
                    result[i] = result[i+1] + 1
                    i -= 1
                if i >= 0 and i+2 <= n-1 and ratings[i] < ratings[i+1]:
                    result[i+1] = max(result[i], result[i+2]) + 1
                i += 1
            i -= 1
        return sum(result)
