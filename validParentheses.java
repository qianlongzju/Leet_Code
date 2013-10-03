import java.util.Vector;
public class Solution {
    public boolean isValid(String s) {
        // Start typing your Java solution below
        // DO NOT write main() function
        Vector<Character> v = new Vector<Character>();
        for (int i=0; i < s.length(); i++) {
            char a = s.charAt(i);
            if (a == '(' || a == '{' || a == '[') {
                v.add(a);
            }
            else {
                if (v.size() == 0) {
                    return false;
                }
                char c = v.lastElement();
                v.remove(v.size()-1);
                if (c == '(' && a == ')') {
                    continue;
                }
                if (c == '{' && a == '}') {
                    continue;
                }
                if (c == '[' && a == ']') {
                    continue;
                }
                return false;
            }
        }
        if (v.size() == 0) {
            return true;
        }
        else {
            return false;
        }
        
    }
}
