class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        result = []
        start, length, count = 0, 0, 0
        s, space = "", " "
        for i in range(len(words)):
            if length + count + len(words[i]) > maxWidth:
                if count == 1:
                    s = words[start]
                    s += space * (maxWidth - len(s))
                else:
                    numSpace = maxWidth - length
                    s = ""
                    for j in range(start, i-1):
                        s += words[j] + space * (numSpace / (count-1))
                        if numSpace%(count-1) != 0:
                            s += space
                            numSpace -= 1
                    s += words[i-1]
                result.append(s)
                length, start, count = len(words[i]), i, 1
            else:
                count += 1
                length += len(words[i])
        s = words[start]
        for j in range(start+1, len(words)):
            s += space + words[j]
        s += space * (maxWidth - len(s))
        result.append(s)
        return result
