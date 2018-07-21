class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        s, stk, begin = "", [], False
        for i in range(len(path)):
            if path[i] == '/':
                begin = False
                if s == '..':
                    if stk:
                        stk.pop(-1)
                elif s == '.':
                    pass
                elif len(s) > 0:
                    stk.append(s)
                s = ""
            elif begin:
                s += path[i]
            else:
                begin = True
                s = "" + path[i]
        if len(path) > 0 and path[-1] != '/':
            if s == '..':
                if stk:
                    stk.pop(-1)
            elif s == '.':
                pass
            else:
                stk.append(s)
        s = ""
        while stk:
            s = stk.pop(-1) + "/" + s
        if len(s) > 1:
            s = s[0:-1]
        if s == '..':
            s = ""
        s = "/" + s
        return s
