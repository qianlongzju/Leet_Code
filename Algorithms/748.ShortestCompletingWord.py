class Solution(object):
    def shortestCompletingWord(self, licensePlate, words):
        """
        :type licensePlate: str
        :type words: List[str]
        :rtype: str
        """
        licensePlate = [c.lower() for c in licensePlate if c.isalpha()]
        #print licensePlate
        def valid(word):
            word = [c.lower() for c in word]
            #print word
            for c in licensePlate:
                if c in word:
                    word.remove(c)
                else:
                    return False
            return True
        result = []
        for word in words:
            if valid(word):
                result.append(word)
        min_length, min_word = len(result[0]), result[0]
        for i in range(1, len(result)):
            if len(result[i]) < min_length:
                min_length, min_word = len(result[i]), result[i]
        return min_word
