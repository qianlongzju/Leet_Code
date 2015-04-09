class Solution:
    # @param A  a list of integers
    # @param m  an integer, length of A
    # @param B  a list of integers
    # @param n  an integer, length of B
    # @return nothing(void)
    def merge(self, A, m, B, n):
        i, j = 0, 0
        C = []
        while i < m and j < n:
            if A[i] < B[j]:
                C.append(A[i])
                i += 1
            else:
                C.append(B[j])
                j += 1
        if i < m:
            C.extend(A[i:])
        if j < n:
            C.extend(B[j:])
        for i in range(m+n):
            A[i] = C[i]
