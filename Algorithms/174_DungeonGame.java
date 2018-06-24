public class Solution {
    public int calculateMinimumHP(int[][] dungeon) {
        int m = dungeon.length;
        int n = dungeon[0].length;
        int[][] cost = new int[m][n];
        cost[m-1][n-1] = Math.max(1, 1 - dungeon[m-1][n-1]);
        for (int i=m-2; i >= 0; i--) {
            int min_HP_on_exit = cost[i+1][n-1];
            cost[i][n-1] = Math.max(min_HP_on_exit - dungeon[i][n-1], 1);
        }
        for (int i=n-2; i >= 0; i--) {
            int min_HP_on_exit = cost[m-1][i+1];
            cost[m-1][i] = Math.max(min_HP_on_exit - dungeon[m-1][i], 1);
        }
        for (int i=m-2; i >= 0; i--) {
        	for (int j=n-2; j >= 0; j--) {
        		int min_HP_on_exit = Math.min(cost[i+1][j], cost[i][j+1]);
                cost[i][j] = Math.max(min_HP_on_exit - dungeon[i][j], 1);
        	}
        }
        return cost[0][0];
    }
}