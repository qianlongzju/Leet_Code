class Solution {
public:
    int calculateMinimumHP(vector<vector<int> > &dungeon) {
    	int m = dungeon.size();
        int n = dungeon[0].size();
        int cost[m][n];
        cost[m-1][n-1] = max(1, 1 - dungeon[m-1][n-1]);
        for (int i=m-2; i >= 0; i--) {
            int min_HP_on_exit = cost[i+1][n-1];
            cost[i][n-1] = max(min_HP_on_exit - dungeon[i][n-1], 1);
        }
        for (int i=n-2; i >= 0; i--) {
            int min_HP_on_exit = cost[m-1][i+1];
            cost[m-1][i] = max(min_HP_on_exit - dungeon[m-1][i], 1);
        }
        for (int i=m-2; i >= 0; i--) {
        	for (int j=n-2; j >= 0; j--) {
        		int min_HP_on_exit = min(cost[i+1][j], cost[i][j+1]);
                cost[i][j] = max(min_HP_on_exit - dungeon[i][j], 1);
        	}
        }
        return cost[0][0];
    }
};