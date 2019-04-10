class Solution:
    # @param dungeon, a list of lists of integers
    # @return a integer
    def calculateMinimumHP(self, dungeon):
        m = len(dungeon)
        n = len(dungeon[0])
        cost = [[0 for i in range(n) ] for j in range(m)]
        cost[m-1][n-1] = max(1, 1 - dungeon[m-1][n-1])
        for i in range(m-2, -1, -1):
            min_HP_on_exit = cost[i+1][n-1]
            cost[i][n-1] = max(min_HP_on_exit - dungeon[i][n-1], 1)
        for i in range(n-2, -1, -1):
            min_HP_on_exit = cost[m-1][i+1]
            cost[m-1][i] = max(min_HP_on_exit - dungeon[m-1][i], 1)
        for i in range(m-2, -1, -1):
            for j in range(n-2, -1, -1):
                min_HP_on_exit = min(cost[i+1][j], cost[i][j+1])
                cost[i][j] = max(min_HP_on_exit - dungeon[i][j], 1)
        return cost[0][0]
