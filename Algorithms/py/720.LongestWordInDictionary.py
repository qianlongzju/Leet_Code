class Solution(object):
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        words.sort(key = lambda x: len(x))
        mapping = {1:set()}
        max_length = 1
        for word in words:
            if len(word) == 1:
                mapping[1].add(word)
            elif len(word)-1 not in mapping:
                break
            elif word[:-1] in mapping[len(word)-1]:
                if len(word) in mapping:
                    mapping[len(word)].add(word)
                else:
                    max_length = len(word)
                    mapping[len(word)] = {word}
        return sorted(list(mapping[max_length]))[0]
