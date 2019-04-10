class Solution(object):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        if len(envelopes) == 0:
            return 0
        envelopes.sort()
        #print envelopes
        number = [1] * len(envelopes)
        for i in range(1, len(envelopes)):
            previous = [number[j] for j in range(i) if envelopes[j][0] < envelopes[i][0] and envelopes[j][1] < envelopes[i][1]]
            if len(previous) != 0:
                number[i] = max(previous) + 1
        #print number
        return max(number)
