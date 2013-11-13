import java.util.*;
public class LRUCache {
    class node {
        int key, value;
        node pre, next;
        node(int k, int v) {
            key = k;
            value = v;
            pre = null;
            next = null;
        }
    }
    public node head, tail;
    public int capacity;
    public int size;
    public HashMap<Integer, node> m;
    public LRUCache(int capacity) {
        this.capacity = capacity;
        size = 0; 
        head = new node(0, 0);
        tail = new node(0, 0);
        head.next = tail;
        tail.pre = head;
        m = new HashMap<Integer, node>();
    }
    
    public int get(int key) {
        if (m.containsKey(key)) {
            node p = m.get(key);
            p.next.pre = p.pre;
            p.pre.next = p.next;
            p.next = head.next;
            head.next.pre = p;
            p.pre = head;
            head.next = p;
            return p.value;
        } else {
            return -1;
        }    
    }
    
    public void set(int key, int value) {
       if (m.containsKey(key)) {
            node p = m.get(key);
            p.next.pre = p.pre;
            p.pre.next = p.next;
            p.next = head.next;
            head.next.pre = p;
            p.pre = head;
            head.next = p;
            p.value = value;
       } else {
           node p = new node(key, value);
           p.next = head.next;
           head.next.pre = p;
           p.pre = head;
           head.next = p;
           m.put(key, p);
           size ++;
           if (size > capacity) {
               p = tail.pre;
               p.pre.next = tail;
               tail.pre = p.pre;
               m.remove(p.key);
               size --;
           }
       } 
    }
}
