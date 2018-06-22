class MyStack {
public:
    /** Initialize your data structure here. */
    MyStack() {
        
    }
    
    /** Push element x onto stack. */
    void push(int x) {
        if (!b.empty()) {
            b.push_back(x);
        } else {
            a.push_back(x);
        }
    }
    
    /** Removes the element on top of the stack and returns that element. */
    int pop() {
        if(!b.empty()) {
            a.swap(b);
        }
        int t;
        while(a.size() > 1) {
            t = a.front();
            a.pop_front();
            b.push_back(t);
        }
        t = a.front();
        a.pop_front();
        return t;
    }
    
    /** Get the top element. */
    int top() {
        if(!b.empty()) {
            a.swap(b);
        }
        int t;
        while(!a.empty()) {
            t = a.front();
            a.pop_front();
            b.push_back(t);
        }
        return t;
    }
    
    /** Returns whether the stack is empty. */
    bool empty() {
        return a.empty() && b.empty();
    }
    deque<int> a, b;
};

/**
 * Your MyStack object will be instantiated and called as such:
 * MyStack obj = new MyStack();
 * obj.push(x);
 * int param_2 = obj.pop();
 * int param_3 = obj.top();
 * bool param_4 = obj.empty();
 */