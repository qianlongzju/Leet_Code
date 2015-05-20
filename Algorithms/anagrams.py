class Solution:
    # @param {string[]} strs
    # @return {string[]}
    def anagrams(self, strs):
        m = collections.defaultdict(list)
        for s in strs:
            m["".join(sorted(s))].append(s)
        result = []
        for key, value in m.items():
            if len(value) > 1:
                result.extend(value)
        return result
