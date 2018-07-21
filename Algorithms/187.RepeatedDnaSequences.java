public class Solution {
    public List<String> findRepeatedDnaSequences(String s) {
        int mapping_size = 4;
        long seq_len = 10;
        int v = 0;
        Set<Integer> keys = new HashSet<Integer>();
        Set<String> result = new HashSet<String>();
        List<String> result2 = new ArrayList<String>();
        for (int i=0; i < s.length(); i ++) {
            int c = 0;
            if (s.charAt(i) == 'A')
                c = 0;
            else if (s.charAt(i) == 'C')
                c = 1;
            else if (s.charAt(i) == 'G')
                c = 2;
            else if (s.charAt(i) == 'T')
                c = 3;
            v = (v * mapping_size + c) & 0xfffff;
            if (i < seq_len - 1)
                continue;
            if (keys.contains(v))
                result.add(s.substring(i-9, i+1));
            else
                keys.add(v);
        }
        for (String t: result) {
            result2.add(t);
        }
        return result2;
    }
}
        
