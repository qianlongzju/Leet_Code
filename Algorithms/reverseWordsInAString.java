//public class Solution {
public class reverseWordsInAString {
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
    public static void main(String[] args) {
    	reverseWordsInAString r = new reverseWordsInAString();
    	System.out.print(r.reverseWords("a b"));
    }
}