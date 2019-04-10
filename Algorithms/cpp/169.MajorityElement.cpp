class Solution {
public:
    int majorityElement(vector<int>& nums) {
        int previous;
        int count = 0;
        for (int i = 0; i < nums.size(); i++) {
            if (count == 0) {
                previous = nums[i];
                count ++;
            } else {
                if (previous == nums[i]) {
                    count ++;
                } else {
                    count --;
                }
            }
        }
        return previous;    
    }
};
