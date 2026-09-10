class Solution(object):
    def splitNum(self, num):
        ans = []
        while num:
            ans.append(num % 10)
            num //= 10
        ans.sort()
        
        num1 = ""
        num2 = ""
        for i in range(len(ans)):
            if i % 2 == 0:
                num1 += str(ans[i])
            if i % 2 == 1:
                num2 += str(ans[i])
        fSum = int(num1) + int(num2)
        return fSum
        
        