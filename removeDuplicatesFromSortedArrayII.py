class Solution:
    def removeDuplicates(self, A):
        n = len(A)
        if n <= 2:
            return n
        j = 1
        for i in range(2, n):
            if A[i] != A[j-1]:
                j += 1
                A[j] = A[i]
        return j+1;
