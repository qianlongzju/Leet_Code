class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        # states 0->1:2 
        #         0->0, 1->0 4 ,1->1, 5
        if board == [] or board[0] == []:
            return
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                count = 0
                for di in [-1, 0, 1]:
                    for dj in [-1, 0, 1]:
                        if di == 0 and dj == 0:
                            continue
                        ii, jj = i+di, j+dj
                        if ii < 0 or ii >= m:
                            continue
                        if jj < 0 or jj >= n:
                            continue
                        if board[ii][jj] in [1, 3]:
                            count += 1
                if board[i][j] == 0 and count == 3:
                    board[i][j] = 2
                elif board[i][j] == 1 and (count < 2 or count > 3):
                    board[i][j] = 3
        for i in range(m):
            for j in range(n):
                if board[i][j] == 3:
                    board[i][j] = 0
                elif board[i][j] == 2:
                    board[i][j] = 1
