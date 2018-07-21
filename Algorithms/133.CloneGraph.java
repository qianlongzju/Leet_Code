/**
 * Definition for undirected graph.
 * class UndirectedGraphNode {
 *     int label;
 *     ArrayList<UndirectedGraphNode> neighbors;
 *     UndirectedGraphNode(int x) { label = x; neighbors = new ArrayList<UndirectedGraphNode>(); }
 * };
 */
public class Solution {
    public UndirectedGraphNode cloneGraph(UndirectedGraphNode graph) {
        if (graph == null) return null;
        Map<UndirectedGraphNode, UndirectedGraphNode> map = new HashMap<>();
        return DFS(graph, map);
    }
    private UndirectedGraphNode DFS(UndirectedGraphNode graph,
            Map<UndirectedGraphNode, UndirectedGraphNode> map) {
        if (map.containsKey(graph)) {
            return map.get(graph);
        }
        UndirectedGraphNode graphCopy = new UndirectedGraphNode(graph.label);
        map.put(graph, graphCopy);
        for (UndirectedGraphNode neighbor : graph.neighbors) {
            graphCopy.neighbors.add(DFS(neighbor, map));
        }
        return graphCopy;
    }
    /*
    //bfs
    public UndirectedGraphNode cloneGraph(UndirectedGraphNode node) {
        if (node == null) return null;
        HashMap<UndirectedGraphNode, UndirectedGraphNode>  map = new HashMap<UndirectedGraphNode, UndirectedGraphNode>();
        LinkedList<UndirectedGraphNode> q = new LinkedList<UndirectedGraphNode>();
        q.add(node);
        UndirectedGraphNode graphCopy = new UndirectedGraphNode(node.label);
        map.put(node, graphCopy);

        while (!q.isEmpty()) {
            node = q.remove();
            for (UndirectedGraphNode neighbor: node.neighbors) {
                if (map.get(neighbor) == null) {
                    UndirectedGraphNode p = new UndirectedGraphNode(neighbor.label);
                    map.put(neighbor, p);
                    q.add(neighbor);
                    map.get(node).neighbors.add(p);
                } else {
                    map.get(node).neighbors.add(map.get(neighbor));
                }
            }
        }
        return graphCopy;
    }
    */
}
