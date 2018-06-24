class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        result = []
        if len(words) == 0:
            return result
        wordLength = len(words[0])
        wordCount = collections.defaultdict(int)
        current = collections.defaultdict(int)
        for word in words:
            wordCount[word] += 1
        for i in range(len(s)-wordLength * len(words)+1):
            current.clear();
            flag = True
            for j in range(len(words)):
                word = s[i + j*wordLength: i + (j+1)*wordLength]
                if word not in wordCount:
                    flag = False
                    break
                current[word] += 1
                if current[word] > wordCount[word]:
                    flag = False
                    break
            if flag:
                result.append(i)
        return result
