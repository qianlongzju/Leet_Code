class MinStack {
private:
    stack<int> data;
    stack<int> min;
public:
    void push(int x) {
        data.push(x);
        if (min.size() > 0 && x > min.top())
            ;
        else
            min.push(x);
    }

    void pop() {
        int temp = data.top();
        data.pop();
        if (temp == min.top())
            min.pop();
    }

    int top() {
       return data.top(); 
    }

    int getMin() {
       return min.top(); 
    }
};
