class StreamChecker(object):

    def __init__(self, words):
        """
        :type words: List[str]
        """
        self.root = {}
        for word in words:
            self.insert(word[::-1])
        self.history = []

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """
        node = self.root
        for c in word:
            if c not in node.keys():
                node[c] = {}
            node = node[c]
        node['is_word'] = True

    def query(self, letter):
        """
        :type letter: str
        :rtype: bool
        """
        node = self.root
        self.history.append(letter)
        i = len(self.history)-1
        while i >= 0:
            c = self.history[i]
            if c in node.keys():
                node = node[c]
                if 'is_word' in node.keys():
                    return True
                i -= 1
            else:
                return False
        return False

# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
