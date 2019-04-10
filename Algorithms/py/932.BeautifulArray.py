class Solution(object):
    def beautifulArray(self, N):
        """
        :type N: int
        :rtype: List[int]
        """
        if N == 1:
            return [1]
        odd = self.beautifulArray((N+1)//2)
        odd = [2*i-1 for i in odd]
        even = self.beautifulArray(N//2)
        even = [2*i for i in even]
        return odd+even
