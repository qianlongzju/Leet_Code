class Solution(object):
    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        same = set('018')
        change = set('2569')
        not_valid = set('347')
        count = 0
        for i in range(1, N+1):
            s = set(str(i))
            if s & not_valid:
                continue
            if s & change:
                count += 1
        return count
