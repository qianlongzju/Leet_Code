class Solution:
    # @param {string} s
    # @param {string} p
    # @return {boolean}
    def isMatch(self, s, p):
        star, i = False, 0
        while i < len(s):
            if i >= len(p):
                if star:
                    s, i = s[1:], -1
                else: 
                    return False
            elif p[i] == '?' or s[i] == p[i]:
                pass
            elif p[i] == '*':
                star = True
                p, s, i = p[i+1:], s[i:], -1
                while p and p[0] == '*':
                    p = p[1:]
                if not p:
                    return True
            elif s[i] != p[i]:
                if star:
                    s, i = s[1:], -1
                else: 
                    return False
            i += 1
        while i < len(p) and p[i] == '*':
            i += 1
        return i == len(p)
