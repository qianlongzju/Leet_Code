public class Solution {
    public String largestNumber(int[] num) {
        List<Integer> new_num = new ArrayList<>();
        for (int i=0; i < num.length; i++) {
            new_num.add(num[i]);
        }
        Collections.sort(new_num, new cmp());
        if (new_num.get(0) == 0)
            return "0";
        String result = "";
        for (int i = 0; i < new_num.size(); i++) {
            result += new_num.get(i);
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
