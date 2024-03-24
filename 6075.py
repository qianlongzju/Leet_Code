class Solution(object):
    def maximumBags(self, capacity, rocks, additionalRocks):
        """
        :type capacity: List[int]
        :type rocks: List[int]
        :type additionalRocks: int
        :rtype: int
        """
        c = 0
        remain = []
        for i in range(len(capacity)):
            if capacity[i] == rocks[i]:
                c += 1
            else:
                remain.append(capacity[i] - rocks[i])
        remain.sort()
        i = 0
        while additionalRocks > 0 and i < len(remain):
            if remain[i] <= additionalRocks:
                additionalRocks -= remain[i]
                i += 1
                c += 1
            else:
                break
        return c
        
