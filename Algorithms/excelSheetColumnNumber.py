class Solution:
    # @param s, a string
    # @return an integer
    def titleToNumber(self, s):
    	table = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    	num = 0
    	for c in s:
    		num = 26*num + table.index(c) + 1
    		num /= 26
    	return num
