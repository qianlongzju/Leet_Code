import java.util.*;
public class Solution {
    public String getPermutation(int n, int k) {
        // Start typing your Java solution below
        // DO NOT write main() function
        ArrayList<Integer> s = new ArrayList<Integer>();
        for (int i=1; i <= n; i++) {
            s.add(i);
        }
        return getPermutation(s, k);
    }
    private String getPermutation(ArrayList<Integer> s, int k) {
        if (s.size() == 1) {
            return s.get(0) + "";
        }
        int p = 1;
        for (int i=2; i <= s.size()-1; i++) {
            p = p*i;
        }
        int a = s.get((k-1)/p);
        k -= ((k-1)/p)*p;
        s.remove(s.indexOf(a));
        return a + getPermutation(s, k);
    }
}
