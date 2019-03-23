class Solution(object):
    def reachNumber(self, target):
        """
        :type target: int
        :rtype: int
        """
        if target == 0:
            return 0
        if target < 0:
            target = -target
        k = 0
        s = 0
        while s < target:
            k += 1
            s += k
        if s == target:
            return k
        diff = s - target
        if diff & 0x01 == 0:
            return k
        if k & 0x01 == 0:
            return k+1
        else:
            return k+2
