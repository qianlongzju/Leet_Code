class Solution(object):
    def numRookCaptures(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                if board[i][j] != 'R':
                    continue
                count = 0
                for di,dj in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                    step = 1
                    while True:
                        ii, jj = i + di*step, j + dj*step
                        step += 1
                        if 0 <= ii < m and 0 <= jj < n:
                            if board[ii][jj] == 'B':
                                break
                            elif board[ii][jj] == 'p':
                                count += 1
                                break
                        else:
                            break
                return count
