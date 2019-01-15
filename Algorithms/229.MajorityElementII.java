class Solution {
    public List<Integer> majorityElement(int[] nums) {
        List<Integer> result = new ArrayList<>();
        Map<Integer, Integer> map = new HashMap<>();
        for (int i=0; i < nums.length; i++) {
          if (map.containsKey(nums[i])) {
            map.put(nums[i], map.get(nums[i]) + 1);
          } else if (map.size() < 2) {
            map.put(nums[i], 1);
          } else {
            for (Integer key: map.keySet()) {
              map.put(key, map.get(key) -1);
            }
            Map<Integer, Integer> new_map = new HashMap<>();
            for (Integer key: map.keySet()) {
              if (map.get(key) != 0) {
                  new_map.put(key, map.get(key));
              }
            }
            map = new_map;
          }
        }
        for (Integer key: map.keySet()) {
          int count = 0;
          for (int i=0; i < nums.length; i++) {
            if (nums[i] == key) {
              count ++;
            }
          }
          if (count * 1.0 / nums.length > 1/3.0) {
            result.add(key);
          }
        }
        return result;
    }
}
