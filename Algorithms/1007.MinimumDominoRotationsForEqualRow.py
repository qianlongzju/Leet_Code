class Solution(object):
    def minDominoRotations(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        d_A = {}
        d_B = {}
        for i in range(1, 7):
            d_A[i] = set()
            d_B[i] = set()
        for i, a in enumerate(A):
            d_A[a].add(i)
        for i, b in enumerate(B):
            d_B[b].add(i)
        min_count = None
        for i in range(1, 7):
            if len(d_A[i].union(d_B[i])) == len(A):
                if min_count == None:
                    #print len(d_A[i]), len(d_B[i]), i
                    min_count = len(A) - max(len(d_A[i]), len(d_B[i]))
                else:
                    min_count = min(min_count, len(A) - max(len(d_A[i]), len(d_B[i])))
        if min_count == None:
            return -1
        return min_count
