public class LRUCache {
    class Node {
        int key, value;
        Node pre, next;
        Node(int k, int v) {
            key = k;
            value = v;
            pre = null;
            next = null;
        }
    }
    public Node head, tail;
    public int capacity;
    public int size;
    public HashMap<Integer, Node> m;
    public LRUCache(int capacity) {
        this.capacity = capacity;
        size = 0; 
        head = new Node(0, 0);
        tail = new Node(0, 0);
        head.next = tail;
        tail.pre = head;
        m = new HashMap<>();
    }
    
    public int get(int key) {
        if (m.containsKey(key)) {
            Node p = m.get(key);
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
    
    public void put(int key, int value) {
       if (m.containsKey(key)) {
            Node p = m.get(key);
            p.next.pre = p.pre;
            p.pre.next = p.next;
            p.next = head.next;
            head.next.pre = p;
            p.pre = head;
            head.next = p;
            p.value = value;
       } else {
           Node p = new Node(key, value);
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
