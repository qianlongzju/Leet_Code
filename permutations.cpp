#include "leetcode.h"
class Solution {
public:
    vector<vector<int> > permute(vector<int> &num) {
        vector<vector<int> > result;
        permute(num, 0, result);
        return result;
    }
    void permute(vector<int> &num, int index,
            vector<vector<int> > &result) {
        // Start typing your C/C++ solution below
        // DO NOT write int main() function
        if (num.size() == index) {
            result.push_back(num);
            return;
        }
        for (int i=index; i < num.size(); ++i) {
            int temp = num[i];
            num[i] = num[index];
            num[index] = temp;
            permute(num, index+1, result);
            temp = num[i];
            num[i] = num[index];
            num[index] = temp;
        }
    }
    //vector<vector<int> > permute(vector<int> &num) {
    //    // Start typing your C/C++ solution below
    //    // DO NOT write int main() function
    //    vector<vector<int> > result;
    //    vector<int> temp;
    //    if (num.size() == 1) {
    //        temp.push_back(num[0]);
    //        result.push_back(temp);
    //        return result;
    //    }
    //    vector<int> sub(num.begin()+1, num.end());
    //    vector<vector<int> > v = permute(sub);
    //    for (int i=0; i < v.size(); ++i) {
    //        for (int j=0; j < v[i].size(); j++) {
    //            temp.clear();
    //            temp = v[i];
    //            int tmp = temp[j];
    //            temp[j] = num[0];
    //            temp.insert(temp.begin(), tmp);
    //            result.push_back(temp);
    //        }
    //        temp = v[i];
    //        temp.insert(temp.begin(), num[0]);
    //        result.push_back(temp);
    //    }
    //    return result;
    //}
    //vector<vector<int> > permute(vector<int> &num) {
    //    // Start typing your C/C++ solution below
    //    // DO NOT write int main() function
    //    vector<vector<int> > result;
    //    vector<int> temp;
    //    if (num.size() == 1) {
    //        temp.push_back(num[0]);
    //        result.push_back(temp);
    //        return result;
    //    }
    //    vector<int> sub(num.begin()+1, num.end());
    //    vector<vector<int> > v = permute(sub);
    //    for (int i=0; i < v.size(); ++i) {
    //        for (int j=0; j <= v[i].size(); j++) {
    //            temp = v[i];
    //            temp.insert(temp.begin()+j, num[0]);
    //            result.push_back(temp);
    //        }
    //    }
    //    return result;
    //}
};
int main() {
    Solution s;
    vector<int> in;
    in.push_back(1);
    in.push_back(2);
    in.push_back(3);
    vector<vector<int> > v;
    v = s.permute(in);
    for (int i=0; i < v.size(); ++i) {
        for (int j=0; j < v[i].size(); j++) {
            cout << v[i][j] << " ";
        }
        cout << endl;
    }
    return 0;
}
