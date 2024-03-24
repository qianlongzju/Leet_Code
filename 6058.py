class Solution(object):
    def __init__(self):
        L = 10**5 + 10
        self.d = [0] * L
        self.f = [0] * L
        self.d[1] = 1
        self.d[2] = 2
        self.d[3] = 4
        self.f[1] = 1
        self.f[2] = 2
        self.f[3] = 4
        self.f[4] = 8
            
    def get_f(self, cnt):
        if self.f[cnt] != 0:
            return self.f[cnt]
        self.f[cnt] = self.get_f(cnt-1) + self.get_f(cnt-2) + self.get_f(cnt-3) + self.get_f(cnt-4)
        return self.f[cnt]
        
    def get_d(self, cnt):
        if self.d[cnt] != 0:
            return self.d[cnt]
        self.d[cnt] = self.get_d(cnt-1) + self.get_d(cnt-2) + self.get_d(cnt-3)
        return self.d[cnt]
        
    def get_comb(self, key, cnt):
        if key == '9' or key == '7':
            return self.get_f(cnt)
        res = self.get_d(cnt)
        return res
    
    def countTexts(self, pressedKeys):
        """
        :type pressedKeys: str
        :rtype: int
        """
        res = 1
        i = 0
        j = 1
        while True:
            if j >= len(pressedKeys):
                #print(j-i, self.get_comb(pressedKeys[i], j-i))
                res *= self.get_comb(pressedKeys[i], j-i)
                break
            if pressedKeys[j] == pressedKeys[i]:
                j += 1
            else:
                #print(j-i, self.get_comb(pressedKeys[i], j-i))
                res *= self.get_comb(pressedKeys[i], j-i)
                i = j
                j = i + 1
        return res % (10**9 + 7)
