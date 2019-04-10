class Solution:
    # @param S, a list of integer
    # @return a list of lists of integer
    def subsets_1(self, S):
        #S.sort()
        results, current = [], []
        def _subsetsHelper(S, pos):
            results.append(current[:])
            for i in range(pos, len(S)):
                current.append(S[i])
                _subsetsHelper(S, i+1)
                current.pop()
        _subsetsHelper(S, 0)
        return results
    
    def subsets_2(self, S):
        return self.subsets_index(S, 0)
    
    def subsets_index(self, S, index):
        if index == len(S):
            return [[]]
        all_subsets = self.subsets_index(S, index+1)
        new_subsets = []
        for subset in all_subsets:
            new_subset = subset[:]
            new_subset.append(S[index])
            new_subsets.append(new_subset)
        all_subsets.extend(new_subsets)
        return all_subsets

    def subsets(self, S):
        result = []
        for i in range(0, pow(2, len(S))):
            subset = []
            j = 0
            while i != 0:
                if i & 0x01 != 0:
                    subset.append(S[j])
                i >>= 1
                j += 1
            result.append(subset)
        return result
