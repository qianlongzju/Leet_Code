class Solution:
    def reorganizeString(self, S: str) -> str:
        c = collections.Counter(S)
        n = len(S)
        res = ""
        if max(c.values())*2 <= n+1:
            while c:
                commons = c.most_common(2)
                if len(commons):
                    res += commons[0][0]
                    c[commons[0][0]] -= 1
                if len(commons) > 1:
                    res += commons[1][0]
                    c[commons[1][0]] -= 1
                c += collections.Counter()
        return res
