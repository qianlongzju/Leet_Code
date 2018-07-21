class Solution {
public:
    string getPermutation(int n, int k) {
        string permutation;
        vector<int> s;
        for (int i=1; i <= n; i++) {
            s.push_back(i);
        }
        getPermutation(s, k, permutation);
        return permutation;
    }
private:
    int factorial(int n) {
        int result = 1;
        for (int i=2; i <= n; ++i) {
            result *= i;
        }
        return result;
    }
    void getPermutation(vector<int>& s, int k, string& permutation) {
        if (s.size() == 1) {
            permutation.push_back(s[0] + '0');
            return;
        }
        int p = factorial(s.size()-1);
        int a = s[(k-1)/p];
        permutation.push_back(a + '0');
        k -= ((k-1)/p)*p;
        s.erase(find(s.begin(), s.end(), a));
        getPermutation(s, k, permutation);
    }
};
