public class Solution {
    public List<Integer> grayCode(int n) {
        List<Integer> v = new ArrayList<>();
        for (int i=0; i < (1<<n); i++) {
            v.add((i >> 1) ^ i);
        }
        return v;
    }
}
