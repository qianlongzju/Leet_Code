class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        if len(board) == 0 or len(board[0]) == 0:
            return []

        self.res = set()

        root = {}
        for word in words:
            node = root
            for c in word:
                if c not in node:
                    node[c] = {}
                node = node[c]
            node['is_word'] = True

        self.m, self.n = len(board), len(board[0])

        for i in range(self.m):
            for j in range(self.n):
                if board[i][j] in root:
                    self._dfs(board, i, j, "", root)
        return list(self.res)
    
    def _dfs(self, board, i, j, cur_word, cur_dict):
        dx, dy = [-1, 1, 0, 0], [0, 0, 1, -1]
        cur_word += board[i][j]
        cur_dict = cur_dict[board[i][j]]
        if 'is_word' in cur_dict:
            self.res.add(cur_word)

        tmp, board[i][j] = board[i][j], '#'
        for k in range(4):
            x, y = i + dx[k], j + dy[k]
            if 0 <= x < self.m and 0 <= y < self.n:
                c = board[x][y]
                if c in cur_dict:
                    self._dfs(board, x, y, cur_word, cur_dict)
        board[i][j] = tmp
