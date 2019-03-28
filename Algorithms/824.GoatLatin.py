class Solution(object):
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        result = []
        for i, word in enumerate(S.split()):
            if word[0].lower() not in 'aeiou':
                word = word[1:] + word[0]
            word += 'ma' + 'a'*(i+1)
            result.append(word)
        return " ".join(result)
