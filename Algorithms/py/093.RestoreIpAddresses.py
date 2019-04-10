class Solution:
    # @param {string} s
    # @return {string[]}
    def restoreIpAddresses(self, s):
        n = len(s)
        result = []
        ipMax = 255
        for i in range(1, 4):
            a = s[:i]
            if a and int(a) > ipMax:
                break
            for j in range(i+1, i+4):
                b = s[i:j]
                if b and int(b) > ipMax:
                    break
                for k in range(j+1, min(j+4, n)):
                    c, d = s[j:k], s[k:]
                    if c and d and int(c) <= ipMax and int(d) <= ipMax:
                        res = ".".join([str(int(l)) for l in (a, b, c, d)])
                        if len(res) == n + 3: result.append(res)
        return result

s = Solution()
print s.restoreIpAddresses("0000")
