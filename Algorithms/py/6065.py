class Solution(object):
    def largestCombination(self, candidates):
        """
        :type candidates: List[int]
        :rtype: int
        """
        ans = 0
        for i in range(25):
            t = 0
            for candidate in candidates:
                if candidate >> i & 0x01 == 1:
                    t += 1
            ans = max(ans, t)
        return ans
