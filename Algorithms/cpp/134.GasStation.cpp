class Solution {
public:
    int canCompleteCircuit(vector<int>& gas, vector<int>& cost) {
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
