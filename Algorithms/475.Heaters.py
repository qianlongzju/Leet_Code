class Solution(object):
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        houses.sort()
        heaters.sort()
        r = 0
        j = 0
        for i in range(len(houses)):
            while j < len(heaters) and heaters[j] < houses[i]:
                j += 1
            if j == len(heaters):
                r = max(r, houses[i] - heaters[j-1])
                continue
            x = abs(houses[i] - heaters[j])
            if j >= 1:
                x = min(x, abs(heaters[j-1] - houses[i]))
            r = max(r, x)
        return r
