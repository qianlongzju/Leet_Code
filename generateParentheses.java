import java.util.*;
public class Solution {
    public ArrayList<String> generateParenthesis(int n) {
        // Start typing your Java solution below
        // DO NOT write main() function
        ArrayList<String> result = new ArrayList<String>();
        String s = "";
        generateParenthesis(n, 0, 0, s, result);
        return result;
    }
    void generateParenthesis(int n, int left, int right, String s,
            ArrayList<String> result) {
        if (left == n && right == n) {
            result.add(s);
            return;
        }
        if (left < n) {
            generateParenthesis(n, left+1, right, s + "(", result);
        }
        if (right < left) {
            generateParenthesis(n, left, right+1, s + ")", result);
        }
    }
}
