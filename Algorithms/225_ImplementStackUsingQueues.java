class MyStack {
    List<Integer> a, b;
    /** Initialize your data structure here. */
    public MyStack() {
        a = new ArrayList<Integer>();
        b = new ArrayList<Integer>();
    }
    
    /** Push element x onto stack. */
    public void push(int x) {
        if (b.size() != 0) {
            b.add(x);
        } else {
            a.add(x);
        }
    }
    
    /** Removes the element on top of the stack and returns that element. */
    public int pop() {
        if (b.size() != 0) {
            a = b;
            b = new ArrayList<Integer>();
        }
        int t;
        while (a.size() > 1) {
            t = a.get(0);
            a.remove(0);
            b.add(t);
        }
        t = a.get(0);
        a.remove(0);
        return t;
    }
    
    /** Get the top element. */
    public int top() {
        if (b.size() != 0) {
            a = b;
            b = new ArrayList<Integer>();
        }
        int t;
        while (a.size() > 1) {
            t = a.get(0);
            a.remove(0);
            b.add(t);
        }
        t = a.get(0);
        a.remove(0);
        b.add(t);
        return t;
    }
    
    /** Returns whether the stack is empty. */
    public boolean empty() {
        return a.size() == 0 && b.size() == 0;
    }
}

/**
 * Your MyStack object will be instantiated and called as such:
 * MyStack obj = new MyStack();
 * obj.push(x);
 * int param_2 = obj.pop();
 * int param_3 = obj.top();
 * boolean param_4 = obj.empty();
 */
