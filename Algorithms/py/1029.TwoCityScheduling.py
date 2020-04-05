class Solution(object):
    def twoCitySchedCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        costs = sorted(costs, key=lambda x:-abs(x[1]-x[0]))
        n = len(costs) / 2
        total = 0
        a, b = 0, 0
        for A, B in costs:
            if (b < n and A > B) or a == n:
                b += 1
                total += B
            else:
                a += 1
                total += A
        return total
