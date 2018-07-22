public class Solution {
    public boolean isValid(String s) {
        Stack<Character> v = new Stack<>();
        Map<Character, Character> map = new HashMap<>() {{
            put('(', ')'); put('{', '}'); put('[', ']');
        }};
        for (Character c: s.toCharArray()) {
            if (map.containsKey(c)) {
                v.push(c);
            }
            else {
                if (v.isEmpty() || map.get(v.pop()) != c ) return false;
            }
        }
        return v.isEmpty();
    }
}
