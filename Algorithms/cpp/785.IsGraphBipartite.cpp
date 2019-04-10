class Solution {
public:
    bool isBipartite(vector<vector<int>>& graph) {
        int N = graph.size();
        int color[N];
        for (int i=0; i < N; i++) {
            color[i] = 0;
        }
        for (int i=0; i < N; i++) {
            if (color[i] == 0 && !dfs(graph, color, i)) {
                return false;
            }
        }
        return true;
    }

private: 
    bool dfs(vector<vector<int>>& graph, int color[], int j) {
        color[j] = 1;
        queue<int> q;
        q.push(j);
        while(!q.empty()) {
            int i = q.front();
            q.pop();
            for (int k=0; k < graph[i].size(); k++) {
                int neighbor = graph[i][k];
                if (color[neighbor] == 0) {
                    q.push(neighbor);
                    color[neighbor] = -color[i];
                }
                else if (color[neighbor] == color[i]) {
                    return false;
                }
            }
        }
        return true;
    }
};
