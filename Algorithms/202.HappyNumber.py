class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        nums = {n}
        while n != 1:
            n = sum(int(c) ** 2 for c in str(n))
            if n in nums:
                return False
            nums.add(n)
        return True
