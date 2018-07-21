class Solution {
public:
    void nextPermutation(vector<int> &num) {
        for (int i=num.size()-1; i > 0; i--) {
            if (num[i] <= num[i-1]) {
                continue;
            }
            for (int j=num.size()-1; j >= i; j--) {
                if (num[j] > num[i-1]) {
                    int temp = num[i-1];
                    num[i-1] = num[j];
                    num[j] = temp;
                    for(int p=i, q=num.size()-1; p < q; p++, q--) {
                        int temp = num[p];
                        num[p] = num[q];
                        num[q] = temp;
                    }
                    return;
                }
            }
        }
        for(int p=0, q=num.size()-1; p < q; p++, q--) {
            int temp = num[p];
            num[p] = num[q];
            num[q] = temp;
        }
    }
};
