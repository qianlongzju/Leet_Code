class Solution {
public:
    vector<int> majorityElement(vector<int>& nums) {
      vector<int> result;
      map<int, int> m;
      for (int i=0; i < nums.size(); i++) {
        if (m.find(nums[i]) != m.end()) {
          m[nums[i]] ++;
        } else if (m.size() < 2) {
          m[nums[i]] = 1;
        } else {
          for (auto j=m.begin(); j != m.end(); j++) {
            j->second --;
          }
          map<int, int> new_m;
          for (auto j=m.begin(); j != m.end(); j++) {
            if (j->second != 0) {
              new_m[j->first] = j->second;
            }
          }
          m = new_m;
        }
      }
      for (auto i=m.begin(); i != m.end(); i++) {
        int count = 0;
        for (int j=0; j < nums.size(); j++) {
          if (nums[j] == i->first) {
            count ++;
          }
        }
        if (count * 1.0 / nums.size() > 1/3.0) {
          result.push_back(i->first);
        }
      }
    return result;
    }
};
