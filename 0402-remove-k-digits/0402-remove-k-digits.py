# class Solution(object):
#     def removeKdigits(self, num, k):
#         stack = []
#         for d in num:
#             while k and stack and stack[-1] > d:
#                 stack.pop()
#                 k -= 1
#             stack.append(d)
            

#         ans = "".join(stack[:-k] if k else stack).lstrip("0")
#         return ans or "0"

class Solution(object):
    def removeKdigits(self, num, k):
        stack = []

        for d in num:
            while k and stack and stack[-1] > d:
                stack.pop()
                k -= 1
            stack.append(d)

        stack = stack[:-k] if k else stack
        ans = "".join(stack)

        while ans and ans[0] == "0":
            ans = ans[1:]

        return ans or "0"