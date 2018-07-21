class Solution {
public:
    int candy(vector<int> &ratings) {
        if (ratings.size() == 1)
            return 1;
        vector<int> result(ratings.size(), 0);
        vector<int> leftToRight(ratings.size(), INT_MIN);
        vector<int> rightToLeft(ratings.size(), INT_MIN);
        // 1:bigger  -1:smaller 0:equal
        leftToRight[0] = 0;
        for (int i=1; i < ratings.size(); i++) {
            if (ratings[i] > ratings[i-1])
                leftToRight[i] = 1;
            else if (ratings[i] < ratings[i-1])
                leftToRight[i] = -1;
            else
                leftToRight[i] = 0;
        }
        rightToLeft[ratings.size()-1] = 0;
        for (int i=ratings.size()-2; i >= 0; i--) {
            if (ratings[i] > ratings[i+1])
                rightToLeft[i] = 1;
            else if (ratings[i] < ratings[i+1])
                rightToLeft[i] = -1;
            else
                rightToLeft[i] = 0;
        }
        for (int i=0; i < ratings.size(); i++)
            if (leftToRight[i] <= 0 && rightToLeft[i] <= 0)
                result[i] = 1;
        for (int i=0; i < ratings.size(); i++)
            if (result[i] == 1) {
                i++;
                while (i < ratings.size() && ratings[i] > ratings[i-1]) {
                    result[i] = result[i-1] + 1;
                    i++;
                }
                i--;
            }
        for (int i=ratings.size()-1; i >= 0; i--)
            if (result[i] == 1) {
                i--;
                while (i >= 0 && ratings[i] > ratings[i+1]) {
                    result[i] = result[i+1] + 1;
                    i--;
                }
                if (i >= 0 && i+2 < ratings.size() && 
                        ratings[i] < ratings[i+1])
                    result[i+1] = (result[i]>result[i+2]?result[i]:result[i+2]) + 1;
                i++;
            }
        int sum = 0; 
        for (int i=0; i < result.size(); i++)
            sum += result[i];
        return sum;
    }
};
