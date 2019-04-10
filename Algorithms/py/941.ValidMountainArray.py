class Solution(object):
    def validMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        if len(A) <= 2:
            return False
        if A[1] <= A[0]:
            return False
        flag = False
        for i in range(1, len(A)):
            if flag == False:
                if A[i] < A[i-1]:
                    flag = True
                elif A[i] == A[i-1]:
                    return False
            elif A[i] >= A[i-1]:
                return False
        return flag == True
