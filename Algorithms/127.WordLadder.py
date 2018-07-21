class Solution:
    # @param beginWord, a string
    # @param endWord, a string
    # @param wordDict, a set<string>
    # @return an integer
    def ladderLength(self, beginWord, endWord, wordDict):
        if beginWord == endWord:
            return 2
        queue = [beginWord]
        mapping = {}
        visited = set()
        while queue:
            tmp = queue.pop(0)
            for i in range(len(tmp)):
                for c in string.lowercase:
                    if c == tmp[i]: continue
                    temp = tmp[:i] + c + tmp[i+1:]
                    if temp == endWord:
                        length = 2
                        while tmp != beginWord:
                            tmp = mapping[tmp]
                            length += 1
                        return length
                    if temp in wordDict and not temp in visited:
                        queue.append(temp)
                        visited.add(temp)
                        mapping[temp] = tmp
        return 0
