import java.util.*;
public class Solution {
    public ArrayList<ArrayList<Integer>> fourSum(int[] num, int target) {
        ArrayList<ArrayList<Integer>> result = new ArrayList<ArrayList<Integer>>();
        HashSet<ArrayList<Integer>> quadplets = new HashSet<ArrayList<Integer>>();
        ArrayList<Integer> quadplet = new ArrayList<Integer>();
        Arrays.sort(num);
        int n = num.length;
        for (int i = 0; i < n; i++) {
            for (int j = i+1; j < n; j++) {
                int k = j + 1;
                int l = n - 1;
                while (k < l) {
                    int sum_four = num[i] + num[j] + num[k] + num[l];
                    if (sum_four < target) {
                        k++;
                    } else if (sum_four > target) {
                        l--;
                    } else {
                        quadplet.add(num[i]);
                        quadplet.add(num[j]);
                        quadplet.add(num[k]);
                        quadplet.add(num[l]);
                        quadplets.add(quadplet);
                        quadplet = new ArrayList<Integer>();
                        k++;
                        l--;
                    }
                }
            }
        }
        for (ArrayList<Integer> a:quadplets)
            result.add(a);
        return result;
    }
}
