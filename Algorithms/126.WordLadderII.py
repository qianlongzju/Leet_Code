class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        wordDict = set(wordList)
        self.result, self.path, self.parents, levels = [], [], {}, {}

        if endWord not in wordDict:
            return self.result
        wordDict.remove(endWord)

        q = [beginWord]
        levels[beginWord] = 1
        level, found = 0, False
        while q and not found:
            level += 1
            for j in range(len(q)):
                tmp = q.pop(0)
                for i in range(len(tmp)):
                    for c in string.lowercase:
                        if c == tmp[i]:
                            continue
                        temp = tmp[:i] + c + tmp[i+1:]
                        if temp == endWord:
                            self.parents.get(endWord, []).append(tmp)
                            found = True
                        elif temp in levels and level < levels[temp]:
                            self.parents.get(temp).append(tmp)
                        if temp not in wordDict:
                            continue
                        wordDict.remove(temp)
                        q.append(temp)
                        levels[temp] = levels[tmp] + 1
                        self.parents[temp] = [tmp]
        if found:
            self.path.append(endWord)
            self.buildPaths(endWord, beginWord)
        return self.result

    def buildPaths(self, word, beginWord):
        if word == beginWord:
            self.result.append(self.path[:])
            return
        for w in self.parents[word]:
            self.path.append(w)
            self.buildPaths(w, beginWord)
            self.path.pop(-1)
