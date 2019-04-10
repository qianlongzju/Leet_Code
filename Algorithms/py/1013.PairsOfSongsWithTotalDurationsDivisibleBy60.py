class Solution(object):
    def numPairsDivisibleBy60(self, time):
        """
        :type time: List[int]
        :rtype: int
        """
        d = {}
        count = 0
        for t in time:
            x = (60-t)%60
            if x in d:
                count += d[x]
            if t%60 in d:
                d[t%60] += 1
            else:
                d[t%60] = 1
        return count 
