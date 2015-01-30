class Solution:
    # @param version1, a string
    # @param version2, a string
    # @return an integer
    def compareVersion(self, version1, version2):
    	version1 = version1.split(".")
    	version2 = version2.split(".")
    	for i in range(max(len(version1), len(version2))):
    		if i >= len(version1):
    			a = 0
    		else:
    			a = int(version1[i])
    		if i >= len(version2):
    			b = 0
    		else:
    			b = int(version2[i])
    		if a > b:
    			return 1
    		elif a < b:
    			return -1
    	return 0


if __name__ == '__main__':
 	s = Solution()
 	print s.compareVersion("1.0", "1")