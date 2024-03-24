class Solution(object):
    def numFlowers(self, roads):
        """
        :type roads: List[List[int]]
        :rtype: int
        """
        d = {}
        for road in roads:
            x, y = road
            if x in d:
                d[x] += 1
            else:
                d[x] = 1
            if y in d:
                d[y] += 1
            else:
                d[y] = 1
        return max(d.values()) + 1
