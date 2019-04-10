class Solution:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}
        
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
        
    def build_trie(self, dict):
        for word in dict:
            self.insert(word)
        
    def replaceWords(self, dict: List[str], sentence: str) -> str:
        self.build_trie(dict)
        sen_list = sentence.split()
        result = []
        for sen in sen_list:
            node = self.root
            for i, c in enumerate(sen):
                if c in node.keys():
                    node = node[c]
                else:
                    result.append(sen)
                    break
                if 'is_word' in node.keys():
                    result.append(sen[:i+1])
                    break
            else:
                result.append(sen)
        return " ".join(result)
