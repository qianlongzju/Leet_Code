class Solution:
    def removeDuplicates(self, A):
        n = len(A)
        if n <= 1:
            return n
        j = 0
        for i in range(1, n):
            if A[i] != A[i-1]:
                j += 1
                A[j] = A[i]
        return j+1;
