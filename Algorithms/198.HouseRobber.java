class Solution {
    public int rob(int[] nums) {
        Map<Integer, Integer> map = new HashMap<>();
        return rob(nums, 0, map);
    }
    private int rob(int[] nums, int index, Map<Integer, Integer> map) {
        if (index >= nums.length) {
            return 0;
        }
        if (map.containsKey(index)) {
            return map.get(index);
        }
        int v = Math.max(nums[index] + rob(nums, index+2, map), rob(nums, index+1, map));
        map.put(index, v);
        return v;
    }
}
