#include "leetcode.h"
class Solution {
public:
    int canCompleteCircuit(vector<int> &gas, vector<int> &cost) {
        // Note: The Solution object is instantiated only once and is reused by each test case.
        int n = gas.size();
        int start = 0;
        int sum = 0;
        int end = start;
        while (true) {
            if (sum + gas[end] < cost[end]) {
                if (end == start) {
                    start ++;
                    end = start;
                    sum = 0;
                } else {
                    sum += cost[start] - gas[start];
                    start ++;
                }
                if (start == n) {
                    return -1;
                }
            } else {
                sum += gas[end] - cost[end];
                end ++;
                if (end == n) {
                    end = 0;
                }
                if (end == start) {
                    return start;
                }
            }
        }
    }
};
int main() {
    Solution s;
    vector<int> gas;
    gas.push_back(2);
    gas.push_back(4);
    vector<int> cost;
    cost.push_back(3);
    cost.push_back(4);
    cout << s.canCompleteCircuit(gas, cost) << endl;
    gas.clear();
    gas.push_back(1);
    gas.push_back(2);
    cost.clear();
    cost.push_back(2);
    cost.push_back(1);
    cout << s.canCompleteCircuit(gas, cost) << endl;
    return 0;
}

