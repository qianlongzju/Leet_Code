class Solution(object):
    def minDeletionSize(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        count = 0
        for i in range(len(A[0])):
            cur = A[0][i]
            flag = True
            for j in range(1, len(A)):
                if ord(A[j][i]) < ord(cur):
                    flag = False
                    break
                cur = A[j][i]
            if flag:
                count += 1
        return len(A[0]) - count
