class Solution:
    # @param S, a list of integer
    # @return a list of lists of integer
    def subsetsWithDup_1(self, S):
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

    def subsetsWithDup_2(self, S):
        S.sort()
        result = set()
        for i in range(0, pow(2, len(S))):
            subset = []
            j = 0
            while i != 0:
                if i & 0x01 != 0:
                    subset.append(S[j])
                i >>= 1
                j += 1
            result.add(tuple(subset))
        return [list(subset) for subset in result]


    def subsetsWithDup(self, S):
        S.sort()
        result = self.subsets_index(S, 0)
        return [list(subset) for subset in result]

    def subsets_index(self, S, index):
        if index == len(S):
            result = set()
            result.add(tuple())
            return result
        all_subsets = self.subsets_index(S, index+1)
        new_subsets = set()
        for subset in all_subsets:
            new_subset = list(subset)
            new_subset.append(S[index])
            new_subsets.add(tuple(new_subset))
        all_subsets = all_subsets.union(new_subsets)
        return all_subsets
