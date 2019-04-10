class Solution(object):
    def ladderLength_bfs(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        wordDict = set(wordList)
        if endWord not in wordDict:
            return 0
        queue, step = [beginWord], 0
        while queue:
            step += 1
            for j in range(len(queue)):
                tmp = queue.pop(0)
                for i in range(len(tmp)):
                    for c in string.lowercase:
                        if c == tmp[i]: continue
                        temp = tmp[:i] + c + tmp[i+1:]
                        if temp == endWord:
                            return step + 1
                        if temp not in wordDict:
                            continue
                        wordDict.remove(temp)
                        queue.append(temp)
        return 0

    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        wordDict = set(wordList)
        if endWord not in wordDict:
            return 0
        q1, q2, step = {beginWord}, {endWord}, 0
        wordDict.remove(endWord)
        while q1 and q2:
            step += 1
            if len(q1) > len(q2):
                q1, q2 = q2, q1
            q = set()
            for j in range(len(q1)):
                tmp = q1.pop()
                for i in range(len(tmp)):
                    for c in string.lowercase:
                        if c == tmp[i]: continue
                        temp = tmp[:i] + c + tmp[i+1:]
                        if temp in q2:
                            return step + 1
                        if temp not in wordDict:
                            continue
                        wordDict.remove(temp)
                        q.add(temp)
            q1 = q
        return 0
