class Solution {
public:
    int threeSumClosest(vector<int> &num, int target) {
        sort(num.begin(), num.end());
        int n = num.size();
        int lowestGap = INT_MAX;
        int closestSum = 0;
        for (int i = 0; i < n; i++) {
            while (i > 0 && i < n && num[i] == num[i-1])
                i++;
            int j = i + 1;
            int k = n - 1;
            while (j < k) {
                int total = num[i] + num[j] + num[k];
                int gap = abs(target - total);
                if (gap < lowestGap) {
                    lowestGap = gap;
                    closestSum = total;
                }
                if (total < target) {
                    j++;
                    while (j < k && num[j] == num[j-1])
                        j++;
                } else if (total > target) {
                    k--;
                    while (k > j && num[k] == num[k+1])
                        k--;
                } else
                    return closestSum;
            }
        }
        return closestSum;
    }
};
int main() {
    Solution s;
    vector<int> v;
    v.push_back(-1);
    v.push_back(2);
    v.push_back(1);
    v.push_back(-4);
    cout << s.threeSumClosest(v, 1) << endl;
    return 0;
}
