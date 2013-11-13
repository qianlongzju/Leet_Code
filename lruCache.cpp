#include "leetcode.h"
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<string> vs;
typedef pair<int, int> ii;
typedef vector<ii> vii;
typedef vector< pair<double,ii> > vdii;
#define sz(a) int((a).size())
#define pb push_back
#define all(c) (c).begin(),(c).end()
#define tr(c,i) for(typeof((c).begin()) i = (c).begin(); i != (c).end(); i++)
#define present(c,x) ((c).find(x) != (c).end())
#define cpresent(c,x) (find(all(c),x) != (c).end())
using namespace std;

struct node {
    int key, value;
    node *pre, *next;
    node(int k, int v): key(k),value(v),pre(NULL),next(NULL) {};
};

class LRUCache{
public:
    node *head, *tail;
    int capacity;
    int size;
    map<int, node*> m;
    LRUCache(int capacity) {
        this->capacity = capacity;
        size = 0; 
        head = new node(0, 0);
        tail = new node(0, 0);
        head->next = tail;
        tail->pre = head;
        m.clear();
    }
    
    int get(int key) {
        if (m.find(key) != m.end()) {
            node *p = m[key];
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
    
    void set(int key, int value) {
       if (m.find(key) != m.end()) {
            node *p = m[key];
            p->next->pre = p->pre;
            p->pre->next = p->next;
            p->next = head->next;
            head->next->pre = p;
            p->pre = head;
            head->next = p;
            p->value = value;
       } else {
           node *p = new node(key, value);
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
