public class Solution {
    public String largestNumber(int[] nums) {
        List<Integer> new_nums = new ArrayList<>();
        for (int i=0; i < nums.length; i++) {
            new_nums.add(nums[i]);
        }
        Collections.sort(new_nums, new cmp());
        if (new_nums.get(0) == 0)
            return "0";
        String result = "";
        for (int i = 0; i < new_nums.size(); i++) {
            result += new_nums.get(i);
        }
        return result;
    }
    class cmp implements Comparator<Integer> {
        @Override
        public int compare(Integer x, Integer y) {
            long i = 10;
            while (i <= y) {
                i *= 10;
            }
            long xx = x*i + y;
            i = 10;
            while (i <= x) {
                i *= 10;
            }
            long yy = y * i + x;
            if (xx < yy)
                return 1;
            return -1;
        }
    }
}
