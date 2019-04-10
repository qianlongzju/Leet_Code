class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        visited = [False] * (n + 1)
        q = [n]
        step = 0
        while q:
            step += 1
            size = len(q)
            
            for i in range(size):
                num = q.pop(0)
                j = 1
                while j * j <= num:
                    a = num - j * j
                    if a < 0:
                        break
                    if a == 0:
                        return step
                    if visited[a] == False:
                        q.append(a)
                        visited[a] = True
                    j += 1
