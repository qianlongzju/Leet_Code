class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if len(a) < len(b):
            a, b = b, a
        m, n, p, s = len(a), len(b), 0, ""
        i = 0
        while i < min(m, n):
            q = ord(a[m-1-i]) - ord('0') + ord(b[n-1-i]) - ord('0') + p
            p = q // 2
            s += str(q%2)
            i += 1
        while i < m:
            q = ord(a[m-1-i]) - ord('0') + p
            p = q // 2
            s += str(q%2)
            i += 1
        if p != 0:
            s += '1'
        return s[::-1]
