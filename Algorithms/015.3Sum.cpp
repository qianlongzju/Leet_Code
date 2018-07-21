class Solution {
public:
    vector<vector<int> > threeSum(vector<int> &num) {
        vector<vector<int> > result;
        set<vector<int> > triplets;
        sort(num.begin(), num.end());
        int n = num.size();
        for (int i = 0; i < n; i++) {
            while (i > 0 && i < n && num[i] == num[i-1])
                i++;
            int j = i + 1;
            int k = n - 1;
            while (j < k) {
                int total = num[i] + num[j] + num[k];
                if (total < 0) {
                    j++;
                    while (j < k && num[j] == num[j-1])
                        j++;
                } else if (total > 0) {
                    k--;
                    while (k > j && num[k] == num[k+1])
                        k--;
                } else {
                    triplets.insert({ num[i], num[j], num[k]});
                    j++;
                    while (j < k && num[j] == num[j-1])
                        j++;
                    k--;
                    while (k > j && num[k] == num[k+1])
                        k--;
                }
            }
        }
        for (auto it=triplets.begin(); it != triplets.end(); ++it)
                result.push_back(*it);
        return result;
    }
};
int main() {
    return 0;
}
