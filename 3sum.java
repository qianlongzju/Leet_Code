import java.util.*;
public class Solution {
    public ArrayList<ArrayList<Integer>> threeSum(int[] num) {
        // Start typing your Java solution below
        // DO NOT write main() function
        ArrayList<ArrayList<Integer>> result = new ArrayList<ArrayList<Integer>>();
        HashSet<ArrayList<Integer>> triplets = new HashSet<ArrayList<Integer>>();
        ArrayList<Integer> triplet = new ArrayList<Integer>();
        Arrays.sort(num);
        int n = num.length;
        for (int i = 0;i < n; i++) {
            int j = i + 1;
            int k = n - 1;
            while (j < k) {
                int sum_three = num[i] + num[j] + num[k];
                if (sum_three < 0) {
                    j++;
                } else if (sum_three > 0) {
                    k--;
                } else {
                    triplet.add(num[i]);
                    triplet.add(num[j]);
                    triplet.add(num[k]);
                    triplets.add(triplet);
                    triplet = new ArrayList<Integer>();
                    j++;
                    k--;
                }
            }
        }
        for (ArrayList<Integer> a:triplets)
            result.add(a);
        return result;
    }
}
