class Solution(object):
    def fairCandySwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        A.sort()
        B.sort()
        a, b = sum(A), sum(B)
        flag = False
        if a > b:
            A, B = B, A
            a, b = b, a
            flag = True
        half = (a + b) / 2
        diff = half - a
        for aa in A:
            i, j = 0, len(B)-1
            while i <= j:
                mid = i + ((j-i) // 2)
                if B[mid] == aa + diff:
                    if flag:
                        return [aa+diff, aa]
                    else:
                        return [aa, aa+diff]
                elif B[mid] < aa + diff:
                    i = mid+1
                else:
                    j = mid-1
