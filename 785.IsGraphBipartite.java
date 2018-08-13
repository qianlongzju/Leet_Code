class Solution {
    public boolean isBipartite(int[][] graph) {
        int N = graph.length;
        int[] color = new int[N];
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

    private boolean dfs(int[][] graph, int[] color, int j) {
        color[j] = 1;
        Queue<Integer> q = new ArrayDeque<>();
        q.offer(j);
        while(q.peek() != null) {
            int i = q.poll();
            for (Integer neighbor: graph[i]) {
                if (color[neighbor] == 0) {
                    q.offer(neighbor);
                    color[neighbor] = -color[i];
                }
                else if (color[neighbor] == color[i]) {
                    return false;
                }
            }
        }
        return true;
    }
}
