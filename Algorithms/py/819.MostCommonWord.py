class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        paragraph = paragraph.replace("!", " ").replace("?", " ").replace("\'", " ")
        paragraph = paragraph.replace(",", " ").replace(";", " ").replace(".", " ")
        counter = collections.defaultdict(int)
        for word in paragraph.split():
            word = word.lower()
            if word not in banned:
                counter[word] += 1
        most, most_count = None, None
        for k, v in counter.items():
            if most_count == None or v > most_count:
                most, most_count = k, v
        return most
