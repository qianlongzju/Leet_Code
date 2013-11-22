#include "leetcode.h"
class Solution {
public:
    UndirectedGraphNode *cloneGraph(UndirectedGraphNode *node) {
        // Note: The Solution object is instantiated only once and is reused by each test case.
        if (!node) return NULL;

        Map map;
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
                // no copy exists
                if (map.find(neighbor) == map.end()) {
                    UndirectedGraphNode *p = new UndirectedGraphNode(neighbor->label);
                    map[node]->neighbors.push_back(p);
                    map[neighbor] = p;
                    q.push(neighbor);
                } else {     // a copy already exists
                    map[node]->neighbors.push_back(map[neighbor]);
                }
            }
        }
        return graphCopy;
    }
};
int main() {
    Solution s;

    return 0;
}

