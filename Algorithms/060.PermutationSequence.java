public class Solution {
    public String getPermutation(int n, int k) {
        ArrayList<Integer> s = new ArrayList<Integer>();
        for (int i=1; i <= n; i++) {
            s.add(i);
        }
        return getPermutation(s, k);
    }
    private int factorial(int n) {
        int result = 1;
        for (int i=2; i <= n; i++) {
            result *= i;
        }
        return result;
    }
    private String getPermutation(ArrayList<Integer> s, int k) {
        if (s.size() == 1) {
            return s.get(0) + "";
        }
        int p = factorial(s.size()-1);
        int a = s.get((k-1)/p);
        k -= ((k-1)/p)*p;
        s.remove(s.indexOf(a));
        return a + getPermutation(s, k);
    }
}
