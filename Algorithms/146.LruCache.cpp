#include "leetcode.h"
struct Node {
    int key, value;
    Node *pre, *next;
    Node(int k, int v): key(k),value(v),pre(NULL),next(NULL) {};
};

class LRUCache{
public:
    Node *head, *tail;
    int capacity;
    int size;
    map<int, Node*> m;
    LRUCache(int capacity) {
        this->capacity = capacity;
        size = 0; 
        head = new Node(0, 0);
        tail = new Node(0, 0);
        head->next = tail;
        tail->pre = head;
        m.clear();
    }
    
    int get(int key) {
        if (m.find(key) != m.end()) {
            Node *p = m[key];
            p->next->pre = p->pre;
            p->pre->next = p->next;
            p->next = head->next;
            head->next->pre = p;
            p->pre = head;
            head->next = p;
            return p->value;
        } else {
            return -1;
        }    
    }
    
    void put(int key, int value) {
       if (m.find(key) != m.end()) {
            Node *p = m[key];
            p->next->pre = p->pre;
            p->pre->next = p->next;
            p->next = head->next;
            head->next->pre = p;
            p->pre = head;
            head->next = p;
            p->value = value;
       } else {
           Node *p = new Node(key, value);
           p->next = head->next;
           head->next->pre = p;
           p->pre = head;
           head->next = p;
           m[key] = p;
           size ++;
           if (size > capacity) {
               p = tail->pre;
               p->pre->next = tail;
               tail->pre = p->pre;
               m.erase(m.find(p->key));
               delete p;
               size --;
           }
       } 
    }
};
int main() {
    return 0;
}
