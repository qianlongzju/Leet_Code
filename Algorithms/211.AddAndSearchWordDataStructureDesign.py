class WordDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: None
        """
        node = self.root
        for c in word:
            if c not in node.keys():
                node[c] = {}
            node = node[c]
        node['is_word'] = True

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        q = [self.root]
        step = 0
        while q:
            size = len(q)
            for i in range(size):
                node = q.pop(0)
                if step == len(word) and 'is_word' in node.keys():
                    return True
                if step == len(word):
                    continue
                if word[step] == '.':
                    for key in node.keys():
                        if key != 'is_word':
                            q.append(node[key])
                elif word[step] in node.keys():
                    q.append(node[word[step]])
            step += 1
            if step == len(word) + 1:
                return False
        return False
                


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
