import java.util.*;
/**
 * Definition for undirected graph.
 * class UndirectedGraphNode {
 *     int label;
 *     ArrayList<UndirectedGraphNode> neighbors;
 *     UndirectedGraphNode(int x) { label = x; neighbors = new ArrayList<UndirectedGraphNode>(); }
 * };
 */
public class Solution {
    public UndirectedGraphNode cloneGraph(UndirectedGraphNode node) {
        // Note: The Solution object is instantiated only once and is reused by each test case.
        if (node == null) return null;

        HashMap<UndirectedGraphNode, UndirectedGraphNode>  map = new HashMap<UndirectedGraphNode, UndirectedGraphNode>();
        LinkedList<UndirectedGraphNode> q = new LinkedList<UndirectedGraphNode>();
        q.add(node);

        UndirectedGraphNode graphCopy = new UndirectedGraphNode(node.label);
        map.put(node, graphCopy);

        while (!q.isEmpty()) {
            node = q.remove();
            int n = node.neighbors.size();
            for (int i = 0; i < n; i++) {
                UndirectedGraphNode neighbor = node.neighbors.get(i);
                // no copy exists
                if (map.get(neighbor) == null) {
                    UndirectedGraphNode p = new UndirectedGraphNode(neighbor.label);
                    map.get(node).neighbors.add(p);
                    map.put(neighbor, p);
                    q.add(neighbor);
                } else {     // a copy already exists
                    map.get(node).neighbors.add(map.get(neighbor));
                }
            }
        }
        return graphCopy;
    }
}
