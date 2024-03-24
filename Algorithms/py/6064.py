class Solution(object):
    def maxConsecutive(self, bottom, top, special):
        """
        :type bottom: int
        :type top: int
        :type special: List[int]
        :rtype: int
        """
        if len(special) == 0:
            return 0
        special = sorted(special)
        #print(special)
        m = special[0] - bottom
        #print(m)
        for i in range(1, len(special)):
            m = max(m, special[i]-special[i-1]-1)
            #print(m)
        m = max(m, top-special[-1])
        return m
            
