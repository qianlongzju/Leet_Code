#include "leetcode.h"
class Solution {
public:
    int maxPoints(vector<Point> &points) {
        // IMPORTANT: Please reset any member data you declared, as
        // the same Solution instance will be reused for each test case.
        int size = points.size();
        if (size <= 2)
            return size;
        map<float, int> slopeMap;
        int maxCount = 0;
        for (int i=0; i < size; ++i) {
            int duplicates = 1;
            int vertical = 0;
            slopeMap.clear();
            for (int j=0; j < size; ++j) {
                if (i == j)
                    continue;
                if (points[i].x == points[j].x && points[i].y == points[j].y) {
                    duplicates ++;
                    continue;
                }
                if (points[i].x == points[j].x)
                    vertical ++;
                else {
                    float k = (points[i].y - points[j].y) * 1.0 / (points[i].x - points[j].x);
                    if (slopeMap.find(k) == slopeMap.end())
                        slopeMap[k] = 1;
                    else 
                        slopeMap[k] ++;
                }
            }
            for (map<float, int>::iterator it = slopeMap.begin(); it != slopeMap.end(); ++it) {
                if (it->second > vertical)
                    vertical = it->second;
            }
            if (vertical + duplicates > maxCount)
                maxCount = vertical + duplicates;
        }
        return maxCount;
    }
};
