class Solution {
public:
    UndirectedGraphNode *cloneGraph(UndirectedGraphNode *node) {
        if (!node) return NULL;
        unordered_map<UndirectedGraphNode *, UndirectedGraphNode *> map;
        return dfs(node, map);
    }
    UndirectedGraphNode *dfs(UndirectedGraphNode* node, unordered_map<UndirectedGraphNode *, UndirectedGraphNode *>& map) {
        if (map.find(node) != map.end()) return map[node];
        UndirectedGraphNode* copyNode = new UndirectedGraphNode(node->label);
        map[node] = copyNode;
        for (int i = 0; i < node->neighbors.size(); i++) {
            copyNode->neighbors.push_back(dfs(node->neighbors[i], map));
        }
        return copyNode;
    }
    /*
    // bfs
    UndirectedGraphNode *cloneGraph(UndirectedGraphNode *node) {
        if (!node) return NULL;
        unordered_map<UndirectedGraphNode *, UndirectedGraphNode *> map;
        queue<UndirectedGraphNode *> q;
        q.push(node);
        UndirectedGraphNode *graphCopy = new UndirectedGraphNode(node->label);
        map[node] = graphCopy;

        while (!q.empty()) {
            node = q.front();
            q.pop();
            int n = node->neighbors.size();
            for (int i = 0; i < n; i++) {
                UndirectedGraphNode *neighbor = node->neighbors[i];
                if (map.find(neighbor) == map.end()) {
                    UndirectedGraphNode *p = new UndirectedGraphNode(neighbor->label);
                    map[neighbor] = p;
                    q.push(neighbor);
                    map[node]->neighbors.push_back(p);
                } else {
                    map[node]->neighbors.push_back(map[neighbor]);
                }
            }
        }
        return graphCopy;
    }
    */
};

