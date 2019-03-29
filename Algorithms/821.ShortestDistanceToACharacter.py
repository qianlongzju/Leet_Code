class Solution(object):
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        c_index = [i for i in range(len(S)) if S[i] == C]
        i, j = 0, 0
        result = []
        while j < len(S):
            if j > c_index[i] and i < len(c_index)-1:
                i += 1
            dist = abs(c_index[i] - j)
            if i > 0:
                dist = min(dist, abs(j-c_index[i-1]))
            result.append(dist)
            j += 1
        return result
