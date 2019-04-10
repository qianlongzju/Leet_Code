class Solution:
    # @param {string} s
    # @param {string} p
    # @return {boolean}
    def isMatch_re(self, s, p):
        return re.match('^' + p + '$', s) != None

    def isMatch_dp(self, s, p):
        """
        f[i][j]: if s[0..i-1] matches p[0..j-1]
        if p[j-1] != '*'
             f[i][j] = f[i-1][j-1] && (s[i-1] == p[j-1] or p[j-1] == '*')
        if p[j-1] == '*', denote p[j-2] with x
             f[i][j] is true iff any of the following is true
             1) "x*" repeats 0 time and matches empty: f[i][j-2]
             2) "x*" repeats >= 1 times and matches "x*x": s[i-1] == x && f[i-1][j]
        '.' matches any single character
        """
        m, n = len(s), len(p)
        f = [[False for i in range(n+1)] for j in range(m+1)]

        f[0][0] = True;
        for i in range(1, m+1):
            f[i][0] = False
        # f[0][j] matches empty iff p[j-1] is '*' and p[0..j-3] matches empty
        for j in range(1, n+1):
            f[0][j] = j > 1 and '*' == p[j-1] and (j < 2 or f[0][j-2])

        for i in range(1, m+1):
            for j in range(1, n+1):
                if p[j-1] != '*':
                    f[i][j] = f[i-1][j-1] and (s[i-1] == p[j-1] or p[j-1] == '.')
                else:
                    # p[0] cannot be '*' so no need to check "j > 1" here
                    f[i][j] = j > 1 and f[i][j-2] or ( (s[i-1] == p[j-2] or '.' == p[j-2]) and f[i-1][j])
        return f[m][n]

    def isMatch_recursively(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if p == s:
            return True
        if s == '':
            return p == '' or (len(p) >= 2 and p[-1] == '*' and self.isMatch(s, p[:-2]))
        if p == '':
            return s == ''
        if p[-1] == s[-1] or p[-1] == '.':
            return self.isMatch(s[:-1], p[:-1])
        if p[-1] == '*':
            if self.isMatch(s, p[:-2]):
                return True
            for i in range(len(s)-1, -1, -1):
                if s[i] == p[-2] or p[-2] == '.':
                    if self.isMatch(s[:i+1], p[:-1]):
                        return True
                else:
                    break
        return False

    def isMatch(self, s, p):
        self.matched = False
        def match(si, pi):
            if self.matched:
                return
            if pi == -1:
                if si == -1:
                    self.matched = True
                return
            if p[pi] == '*':
                #print 'a', si, pi-2
                match(si, pi-2)
                for k in range(si+1):
                    #print 'b', si-k, pi-1
                    if s[si-k] == p[pi-1] or p[pi-1] == '.':
                        match(si-k, pi-1)
                    else:
                        break
            elif si != -1 and (p[pi] == '.' or p[pi] == s[si]):
                match(si-1, pi-1)
        match(len(s)-1, len(p)-1)
        return self.matched
