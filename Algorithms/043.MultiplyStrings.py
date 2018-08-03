class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        m, n = len(num1), len(num2)
        result = [0] * (m+n)
        for i in range(m):
            p = 0
            for j in range(n):
                q = result[i+j] + int(num1[m-1-i]) * int(num2[n-1-j]) + p
                p, result[i+j] = q / 10, q % 10
            if p:
                result[i+n] += p
                p = 0
        if p: 
            result[m+n-1] += p
        s = ""
        i = m+n-1
        while i >= 0 and result[i] == 0:
            i -= 1
        result = result[:i+1][::-1]
        s = "".join(map(str, result))
        if s == "":
            s = "0"
        return s
