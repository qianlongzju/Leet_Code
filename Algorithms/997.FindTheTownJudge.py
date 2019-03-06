class Solution(object):
    def findJudge(self, N, trust):
        """
        :type N: int
        :type trust: List[List[int]]
        :rtype: int
        """
        me_trust_other = [set() for i in range(N)]
        other_trust_me = [set() for i in range(N)]
        for a, b in trust:
            me_trust_other[a-1].add(b-1)
            other_trust_me[b-1].add(a-1)
        for i in range(N):
            if len(me_trust_other[i]) == 0 and len(other_trust_me[i]) == N-1:
                return i + 1
        return -1
