
class MedianFinder {
public:
    /** initialize your data structure here. */
    MedianFinder() {
        
    }
    
    void addNum(int num) {
        if (upper.size() == 0) {
            upper.push_back(num);
        } else if (upper.size() == lower.size()) {
            if (num > lower[0]) {
                upper.push_back(num);
                push_heap(upper.begin(), upper.end(), greater<int>());
            } else {
                lower.push_back(num);
                push_heap(lower.begin(), lower.end());
                int val = lower[0];
                pop_heap(lower.begin(), lower.end());
                lower.pop_back();
                upper.push_back(val);
                push_heap(upper.begin(), upper.end(), greater<int>());
            }
        } else {
            if (num > upper[0]) {
                upper.push_back(num);
                push_heap(upper.begin(), upper.end(), greater<int>());
                int val = upper[0];
                pop_heap(upper.begin(), upper.end(), greater<int>());
                upper.pop_back();
                lower.push_back(val);
                push_heap(lower.begin(), lower.end());
            } else {
                lower.push_back(num);
                push_heap(lower.begin(), lower.end());
            }
        }
    }
    
    double findMedian() {
        //cout << upper.size() << " " << lower.size() << endl;
        if ((upper.size() + lower.size()) & 0x01 == 1) {
            return upper[0];
        } else {
            return (upper[0] + lower[0]) / 2.0;
        }
    }
private:
    vector<int> lower, upper;
};

/**
 * Your MedianFinder object will be instantiated and called as such:
 * MedianFinder obj = new MedianFinder();
 * obj.addNum(num);
 * double param_2 = obj.findMedian();
 */
