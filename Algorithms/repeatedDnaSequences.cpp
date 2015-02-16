class Solution {
public:
    vector<string> findRepeatedDnaSequences(string s) {
    	int mapping_size = 4;
    	long seq_len = 10;
    	int v = 0;
    	set<long> keys;
    	set<string> result;
    	vector<string> result2;
        for (int i=0; i < s.size(); i ++) {
        	int c = 0;
        	if (s[i] == 'A')
        		c = 0;
        	else if (s[i] == 'C')
        		c = 1;
        	else if (s[i] == 'G')
        		c = 2;
        	else if (s[i] == 'T')
        		c = 3;
        	v = (v * mapping_size + c) & 0xfffff;
        	if (i < seq_len - 1)
        		continue;
        	if (keys.find(v) != keys.end())
        		result.insert(s.substr(i-9, 10));
        	else
        		keys.insert(v);
        }
        for (set<string>::iterator it=result.begin(); it != result.end(); it++) {
        	result2.push_back(*it);
        }
        return result2;
    }
};
