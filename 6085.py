class Solution(object):
    def maximumImportance(self, n, roads):
        """
        :type n: int
        :type roads: List[List[int]]
        :rtype: int
        """
        data = [0] * n
        for road in roads:
            a, b = road
            data[a] += 1
            data[b] += 1
        data = sorted(data)
        s = 0
        for i in range(len(data)):
            s += (i+1) * data[i]
        return s
