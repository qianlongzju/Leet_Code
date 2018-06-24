import java.util.Stack;
class MinStack {
    private Stack<Integer> data;
    private Stack<Integer> min;
    public MinStack() {
        data = new Stack<Integer>();
        min = new Stack<Integer>();
    }
    public void push(int x) {
        data.push(x);
        if (!min.empty() && x > min.peek())
            ;
        else 
            min.push(x); 
    }

    public void pop() {
        int temp = data.peek();
        data.pop();
        if (temp == min.peek())
            min.pop();
    }

    public int top() {
        return data.peek(); 
    }

    public int getMin() {
        return min.peek();        
    }
}
