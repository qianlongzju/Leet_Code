#include "leetcode.h"
class Solution {
public:
    int candy(vector<int> &ratings) {
        // Note: The Solution object is instantiated only once and is reused by each test case.
        if (ratings.size() == 1) {
            return 1;
        }
        vector<int> result(ratings.size(), 0);
        vector<int> leftToRight(ratings.size(), INT_MIN);
        vector<int> rightToLeft(ratings.size(), INT_MIN);
        // 1:bigger  -1:smaller 0:equal
        leftToRight[0] = 0;
        for (int i=1; i < ratings.size(); i++) {
            if (ratings[i] > ratings[i-1]) {
                leftToRight[i] = 1;
            } else if (ratings[i] < ratings[i-1]) {
                leftToRight[i] = -1;
            } else {
                leftToRight[i] = 0;
            }
        }
        rightToLeft[ratings.size()-1] = 0;
        for (int i=ratings.size()-2; i >= 0; i--) {
            if (ratings[i] > ratings[i+1]) {
                rightToLeft[i] = 1;
            } else if (ratings[i] < ratings[i+1]) {
                rightToLeft[i] = -1;
            } else {
                rightToLeft[i] = 0;
            }
        }
        for (int i=0; i < ratings.size(); i++) {
            if (leftToRight[i] <= 0 && rightToLeft[i] <= 0) {
                result[i] = 1;
            }
        }
        //for (int i=0; i < result.size(); i++) {
        //    cout << result[i] << " ";
        //}
        //cout << endl;
        for (int i=0; i < ratings.size(); i++) {
            if (result[i] == 1) {
                i++;
                while (i < ratings.size() && ratings[i] > ratings[i-1]) {
                    result[i] = result[i-1] + 1;
                    i++;
                }
                i--;
            }
        }
        //for (int i=0; i < result.size(); i++) {
        //    cout << result[i] << " ";
        //}
        //cout << endl;
        for (int i=ratings.size()-1; i >= 0; i--) {
            if (result[i] == 1) {
                i--;
                while (i >=0 && ratings[i] > ratings[i+1]) {
                    result[i] = result[i+1] + 1;
                    i--;
                }
                if (i >= 0 && i+2 < ratings.size() && ratings[i] < ratings[i+1]) {
                    result[i+1] = (result[i]>result[i+2]?result[i]:result[i+2]) + 1;
                }
                i++;
            }
        }
        //for (int i=0; i < result.size(); i++) {
        //    cout << result[i] << " ";
        //}
        //cout << endl;
        int sum = 0; 
        for (int i=0; i < result.size(); i++) {
            sum += result[i];
        }
        return sum;
    }
};
int main() {
    Solution s;
    vector<int> a;
    a.push_back(1);
    a.push_back(2);
    a.push_back(3);
    a.push_back(4);
    a.push_back(2);
    a.push_back(6);
    cout << "13: " << endl << s.candy(a) << endl;
    vector<int> b;
    b.push_back(2);
    cout << "1: " << endl << s.candy(b) << endl;
    vector<int> c;
    c.push_back(2);
    c.push_back(2);
    cout << "2: " << endl << s.candy(c) << endl;
    vector<int> d;
    d.push_back(2);
    d.push_back(3);
    d.push_back(2);
    cout << "4: " << endl << s.candy(d) << endl;
    vector<int> e;
    e.push_back(2);
    e.push_back(2);
    e.push_back(1);
    cout << "4: " << endl << s.candy(e) << endl;
    vector<int> f;
    f.push_back(1);
    f.push_back(1);
    f.push_back(1);
    f.push_back(1);
    cout << "4: " << endl << s.candy(f) << endl;
    //5,1,1,1,10,2,1,1,1,3
    vector<int> g;
    g.push_back(5);
    g.push_back(1);
    g.push_back(1);
    g.push_back(1);
    g.push_back(10);
    g.push_back(2);
    g.push_back(1);
    g.push_back(1);
    g.push_back(1);
    g.push_back(3);
    cout << "15: " << endl << s.candy(g) << endl;
    return 0;
}

