public class Solution {
    public String reverseWords(String s) {
        s = s.trim();
        if (s.equals(""))
            return "";
        String[] t = s.split(" +");
        s = t[t.length-1];
        for (int i = t.length-2; i >= 0; i--) {
            s = s + " " + t[i];
        }
        return s;
    }
}
