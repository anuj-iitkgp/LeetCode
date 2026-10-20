class Solution(object):
    def removeKdigits(self, num, k):
        stack = []
        for d in num:
            while k and stack and stack[-1] > d:
                stack.pop()
                k -= 1
            stack.append(d)
            

        ans = "".join(stack[:-k] if k else stack).lstrip("0")
        return ans or "0"