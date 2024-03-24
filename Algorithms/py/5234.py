class Solution(object):
    def removeAnagrams(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        result = []
        for word in words:
            if len(result) == 0:
                result.append(word)
            elif sorted(word) == sorted(result[-1]):
                continue
            else:
                result.append(word)
        return result
        # d = {}
        # for i, word in enumerate(words):
        #     if "".join(sorted(word)) in d:
        #         continue
        #     d["".join(sorted(word))] = i, word
        # return [x[1] for x in sorted(d.values(), key=lambda x: x[0])]
