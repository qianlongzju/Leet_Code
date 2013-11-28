import java.util.*;
public class Solution {
    public int evalRPN(String[] tokens) {
        // IMPORTANT: Please reset any member data you declared, as
        // the same Solution instance will be reused for each test case.
        Stack<Integer> stk = new Stack<Integer>();
        for (int i=0; i < tokens.length; ++i) {
            if (tokens[i].equals("+")) {
                int a = stk.peek();
                stk.pop();
                int b = stk.peek();
                stk.pop();
                stk.push(b + a);
            } else if (tokens[i].equals("-")) {
                int a = stk.peek();
                stk.pop();
                int b = stk.peek();
                stk.pop();
                stk.push(b - a);
            } else if (tokens[i].equals("*")) {
                int a = stk.peek();
                stk.pop();
                int b = stk.peek();
                stk.pop();
                stk.push(b * a);
            } else if (tokens[i].equals("/")) {
                int a = stk.peek();
                stk.pop();
                int b = stk.peek();
                stk.pop();
                stk.push(b / a);
            } else {
                stk.push(Integer.parseInt(tokens[i]));
            }
        }
        return stk.peek();
    }
}
