class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        return [a for a in A if a&0x01 == 0] + [a for a in A if a&0x01==1]
