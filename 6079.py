class Solution(object):
    def discountPrices(self, sentence, discount):
        """
        :type sentence: str
        :type discount: int
        :rtype: str
        """
        words = sentence.split(" ")
        for i in range(len(words)):
            word = words[i]
            if word.startswith('$') and word[1:].isdigit():
                word = '$' + format(float(word[1:]) * (1 - discount*1.0/100), '.2f')
                words[i] = word
        return " ".join(words)
