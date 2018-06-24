public class Solution {
    public int evalRPN(String[] tokens) {
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
