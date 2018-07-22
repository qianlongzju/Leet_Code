class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        n, start, end, S = len(gas), 0, 0, 0
        while True:
            if S + gas[end] < cost[end]:
                if end == start:
                    start += 1
                    end = start
                    S = 0
                else:
                    S += cost[start] - gas[start]
                    start += 1
                if start == n: 
                    return -1
            else:
                S += gas[end] - cost[end]
                end += 1
                if end == n:
                    end = 0
                if end == start:
                    return start
