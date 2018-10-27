class Solution:
    # @param S, a list of integer
    # @return a list of lists of integer
    def subsetsWithDup(self, S):
        def _subsetsHelper(S, pos):
            results.append(current[:])
            for i in range(pos, len(S)):
                if i != pos and S[i] == S[i-1]: continue
                current.append(S[i])
                _subsetsHelper(S, i+1)
                current.pop()
        S.sort()
        results, current = [], []
        _subsetsHelper(S, 0)
        return results

