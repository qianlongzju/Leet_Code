class Solution(object):
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        increase = None
        for i in range(1, len(A)):
            if A[i] > A[i-1]:
                if increase == False:
                    return False
                increase = True
            elif A[i] < A[i-1]:
                if increase == True:
                    return False
                increase = False
        return True
