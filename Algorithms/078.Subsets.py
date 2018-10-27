class Solution:
    # @param S, a list of integer
    # @return a list of lists of integer
    def subsets(self, S):
        S.sort()
        results, current = [], []
        def _subsetsHelper(S, pos):
            results.append(current[:])
            for i in range(pos, len(S)):
                current.append(S[i])
                _subsetsHelper(S, i+1)
                current.pop()
        _subsetsHelper(S, 0)
        return results

