public class Solution {
    public int gcd(int a, int b) {
        return (b == 0) ? a : gcd(b, a % b);
    }   
    public int maxPoints(Point[] points) {
        int size = points.length;
        if (size <= 2)
            return size;
        Map<Map<Integer, Integer>, Integer> slopeMap = new HashMap<>();
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
                int d = gcd(dy, dx);
                Map<Integer, Integer> t = new HashMap<>();
                t.put(dx / d, dy / d);
                slopeMap.put(t, slopeMap.getOrDefault(t, 0) + 1);
            }
            for(int value: slopeMap.values()) {
                if (value > vertical)
                    vertical = value;
            }
            maxCount = Integer.max(vertical + duplicates, maxCount);
        }
        return maxCount;
    }
}
