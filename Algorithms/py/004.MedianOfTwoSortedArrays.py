class Solution:
    # @return a float
    def findMedianSortedArrays(self, A, B):
        def _find_kth(A, B, k):
            #always assume that m is equal or smaller than n
            m = len(A)
            n = len(B)
            if m > n: return _find_kth(B, A, k)
            if m == 0: return B[k - 1]
            if k == 1: return min(A[0], B[0])
            #divide k into two parts
            pa = min(k >> 1, m)
            pb = k - pa
            if A[pa - 1] < B[pb - 1]:
                return _find_kth(A[pa:], B, k - pa)
            elif (A[pa - 1] > B[pb - 1]):
                return _find_kth(A, B[pb:], k - pb)
            else:
                return A[pa - 1]

        total = len(A) + len(B)
        if total % 2:
            return _find_kth(A, B, (total >> 1) + 1)
        else:
            return (_find_kth(A, B, total >> 1)
                    + _find_kth(A, B, (total >> 1) + 1)) / 2.0
