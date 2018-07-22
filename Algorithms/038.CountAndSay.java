public class Solution {
    public String countAndSay(int n) {
        List<Integer> v = new ArrayList<>();
        List<Integer> w = new ArrayList<>();
        String result = "";
        v.add(1);
        while (--n > 0) {
            int count = 1;
            for (int i=1; i < v.size(); ++i)
            {
                if (v.get(i) == v.get(i-1)) {
                    count ++;
                }
                else {
                    w.add(count);
                    w.add(v.get(i-1));
                    count = 1;
                }
            }
            w.add(count);
            w.add(v.get(v.size()-1));
            v = w;
            w = new ArrayList<>();
        }
        for (int i = 0; i < v.size(); ++i)
        {
            result += v.get(i);
        }
        return result;
    }
}
