class Solution(object):
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        n = len(bits)
        i = 0
        while i < n:
            if bits[i] == 0 and i == n-1:
                return True
            elif bits[i] == 0:
                i += 1
            else:
                i += 2
        return False
