class Solution {
public:
    vector<vector<int> > fourSum(vector<int> &num, int target) {
        vector<vector<int> > result;
        sort(num.begin(), num.end());
        set<vector<int> > quadplets;
        int n = num.size();
        for (int i = 0; i < n; i++) {
            for (int j = i+1; j < n; j++) { 
                int k = j + 1;
                int l = n - 1;
                while (k < l) {
                    int sum_four = num[i] + num[j] + num[k] + num[l];
                    if (sum_four < target) {
                        k++;
                    } else if (sum_four > target) {
                        l--;
                    } else {
                        quadplets.insert({num[i], num[j], num[k], num[l]);
                        k++;
                        l--;
                    }
                }
            }
        }
        for (auto it=quadplets.begin(); it != quadplets.end(); ++it)
                result.push_back(*it);
        return result;
    }
};
int main() {
    vector<int> a;
    a.push_back(2);
    a.push_back(1);
    a.push_back(0);
    a.push_back(-1);
    Solution s;
    vector<vector<int> > v = s.fourSum(a, 2);
    for (int i=0; i < v.size(); i++) {
        cout << v[i][0] << " " << v[i][1] << " " << v[i][2] << " " << v[i][3] << endl;
    }
    return 0;
}
