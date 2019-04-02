class Solution(object):
    def canThreePartsEqualSum(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        s = sum(A)
        if s % 3 != 0 or len(A) < 3:
            return False
        t = 0
        c = 0
        for i in range(len(A)):
            t += A[i]
            if t == s/3:
                t = 0
                c += 1
                if c == 3:
                    return sum(A[i+1:]) == 0
        return False
