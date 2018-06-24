import java.util.Arrays;
import java.util.Comparator;
import java.util.*;
public class Solution {
    public String largestNumber(int[] num) {
        List<Integer> new_num = new ArrayList<Integer>();
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
    public static void main(String[] args) {
        Solution s = new Solution();
        int[] a = {0,9,8,7,6,5,4,3,2,1};
        System.out.println(s.largestNumber(a));
    }
}