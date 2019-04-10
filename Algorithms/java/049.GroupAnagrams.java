class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        List<List<String>> result = new ArrayList<List<String>>();
        Map<String, List<String>> m = new HashMap<String, List<String>>();
        for (int i=0; i < strs.length; ++i) {
            char[] chars = strs[i].toCharArray();
            Arrays.sort(chars);
            String temp = new String(chars);
            if (m.get(temp) == null) {
                List<String> a = new ArrayList<>();
                a.add(strs[i]);
                m.put(temp, a);
            } else {
                m.get(temp).add(strs[i]);
            }
        }
        for (List<String> it: m.values()) {
            result.add(it);
        }
        return result;
    }
}
