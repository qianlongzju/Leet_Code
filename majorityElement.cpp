class Solution {
public:
    int majorityElement(vector<int> &num) {
    	int previous;
    	int count = 0;
    	for (int i = 0; i < num.size(); i++) {
    		if (count == 0) {
    			previous = num[i];
    			count ++;
    		} else {
    			if (previous == num[i]) {
    				count ++;
    			} else {
    				count --;
    			}
    		}
    	}
    	return previous;    
    }
};