class Solution:
    def kthGrammar(self, N: int, K: int) -> int:
        t = ["01", "10"]
        if N == 1:
            return 0
        a = (K+1) // 2
        r = self.kthGrammar(N-1, a)
        b = t[r]
        if K % 2 == 1:
            return int(b[0])
        else:
            return int(b[1])
