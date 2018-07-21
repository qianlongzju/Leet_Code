public class Solution {
    public ArrayList<ArrayList<Integer>> threeSum(int[] num) {
        ArrayList<ArrayList<Integer>> result = new ArrayList<ArrayList<Integer>>();
        HashSet<ArrayList<Integer>> triplets = new HashSet<ArrayList<Integer>>();
        ArrayList<Integer> triplet = new ArrayList<Integer>();
        Arrays.sort(num);
        int n = num.length;
        for (int i = 0; i < n; i++) {
            while (i > 0 && i < n && num[i] == num[i-1])
                i++;
            int j = i + 1;
            int k = n - 1;
            while (j < k) {
                int total = num[i] + num[j] + num[k];
                if (total < 0) {
                    j++;
                    while (j < k && num[j] == num[j-1])
                        j++;
                } else if (total > 0) {
                    k--;
                    while (k > j && num[k] == num[k+1])
                        k--;
                } else {
                    triplet.add(num[i]);
                    triplet.add(num[j]);
                    triplet.add(num[k]);
                    triplets.add(triplet);
                    triplet = new ArrayList<Integer>();
                    j++;
                    while (j < k && num[j] == num[j-1])
                        j++;
                    k--;
                    while (k > j && num[k] == num[k+1])
                        k--;
                }
            }
        }
        for (ArrayList<Integer> a:triplets)
            result.add(a);
        return result;
    }
}
