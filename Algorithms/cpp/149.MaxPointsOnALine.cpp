class Solution {
public:
    int gcd(int a, int b) {
        return (b == 0) ? a : gcd(b, a % b);
    }
    int maxPoints(vector<Point>& points) {
        int size = points.size();
        if (size <= 2)
            return size;
        map<pair<int, int>, int> slopeMap;
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
                if (points[i].x == points[j].x) {
                    vertical ++;
                    continue;
                }
                int dy = points[i].y - points[j].y;
                int dx = points[i].x - points[j].x;
                int d = gcd(dx, dy);
                slopeMap[{dx / d, dy / d}] ++;
            }
            for (auto it = slopeMap.begin(); it != slopeMap.end(); ++it) {
                if (it->second > vertical)
                    vertical = it->second;
            }
            maxCount = max(vertical + duplicates, maxCount);
        }
        return maxCount;
    }
};
