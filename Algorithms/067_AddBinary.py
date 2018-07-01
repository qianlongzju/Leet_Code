class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        m, n, p, s = len(a), len(b), 0, ""
        i = 0
        while i < min(m, n):
            q = ord(a[m-1-i]) - ord('0') + ord(b[n-1-i]) - ord('0') + p
            p = q / 2
            if q%2 == 1:
                s = '1' + s
            else:
                s = '0' + s
            i += 1
        while i < m:
            q = ord(a[m-1-i]) - ord('0') + p
            p = q / 2
            if q%2 == 1:
                s = '1' + s
            else:
                s = '0' + s
            i += 1
        while i < n:
            q = ord(b[n-1-i]) - ord('0') + p
            p = q / 2
            if q%2 == 1:
                s = '1' + s
            else:
                s = '0' + s
            i += 1
        if p != 0:
            s = '1' + s
        return s
