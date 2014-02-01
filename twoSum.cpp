#include "leetcode.h"
class Solution {
    public:
        vector<int> twoSum(vector<int> &numbers, int target) {
            vector<int> result;
            unordered_map<int, int> mapping;
            for (int i=0; i < numbers.size(); i++) 
                mapping[numbers[i]] = i;
            for (int i = 0; i < numbers.size(); i++) {
                int gap = target - numbers[i];
                if (mapping.find(gap) != mapping.end() &&
                        mapping[gap] != i) {
                    result.push_back(i + 1);
                    result.push_back(mapping[gap] + 1);
                    break;
                }
            }
            return result;
        }
};
