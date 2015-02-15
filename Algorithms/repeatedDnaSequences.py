class Solution:
    # @param s, a string
    # @return a list of strings
    def findRepeatedDnaSequences(self, s):
    	mapping = {'A': 0, 'C': 1, 'G': 2, 'T':3}
    	mapping_size = len(mapping)
    	seq_len = 10
    	v = 0
    	keys = set()
    	result = set()
        for i, c in enumerate(s):
        	v = (v * mapping_size + mapping[c]) & 0xfffff
        	if i < seq_len - 1:
        		continue
        	if v in keys:
        		result.add(s[i-9:i+1])
        	else:
        		keys.add(v)
        return list(result)

if __name__ == '__main__':
	s = Solution()
	print s.findRepeatedDnaSequences("AAAAAAAAAAA")
