class Solution(object):
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        gap = 0
        prev = -1
        for i, seat in enumerate(seats):
            if seat == 1:
                if prev == -1:
                    gap = i
                else:
                    gap = max(gap, (i-prev) // 2)
                prev = i
            elif i == len(seats)-1:
                gap = max(gap, i-prev)
        return gap
