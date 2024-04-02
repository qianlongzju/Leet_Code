class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        result = []
        wordLength = len(words[0])
        wordCount = collections.defaultdict(int)
        current = collections.defaultdict(int)
        for word in words:
            wordCount[word] += 1
        for i in range(len(s)-wordLength * len(words)+1):
            current.clear();
            for j in range(len(words)):
                word = s[i + j*wordLength: i + (j+1)*wordLength]
                if word not in wordCount:
                    break
                current[word] += 1
                if current[word] > wordCount[word]:
                    break
            else:
                result.append(i)
        return result