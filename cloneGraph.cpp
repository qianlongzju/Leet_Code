#include "leetcode.h"
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<string> vs;
typedef pair<int, int> ii;
typedef vector<ii> vii;
typedef vector< pair<double,ii> > vdii;
#define sz(a) int((a).size())
#define pb push_back
#define all(c) (c).begin(),(c).end()
#define tr(c,i) for(typeof((c).begin()) i = (c).begin(); i != (c).end(); i++)
#define present(c,x) ((c).find(x) != (c).end())
#define cpresent(c,x) (find(all(c),x) != (c).end())
typedef map<UndirectedGraphNode*, UndirectedGraphNode*> Map;
using namespace std;
/**
 * Definition for undirected graph.
 * struct UndirectedGraphNode {
 *     int label;
 *     vector<UndirectedGraphNode *> neighbors;
 *     UndirectedGraphNode(int x) : label(x) {};
 * };
 */
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

