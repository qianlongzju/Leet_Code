class Solution {
public:
    vector<int> grayCode(int n) {
        vector<int> v;
        for (int i=0; i < (1<<n); i++) {
            v.push_back((i >> 1) ^ i);
        }
        return v;
    }
};
int main() {
    Solution s;
    vector<int> v = s.grayCode(2);
    for (int i=0; i < v.size(); ++i) {
        cout << v[i] << " ";
    }
    cout << endl;
    return 0;
}
