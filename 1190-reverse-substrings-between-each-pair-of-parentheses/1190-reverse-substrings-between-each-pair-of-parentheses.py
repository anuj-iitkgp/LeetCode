class Solution(object):
    def reverseParentheses(self, s):
        n = len(s)
        a = []
        t = []
        for i in range(n):
            if s[i] == '(':
                a.append(len(t))
            elif s[i] == ')':
                u = a.pop()
                t[u:] = t[u:][::-1]
            else:
                t.append(s[i])
        return "".join(t)

 
        

        