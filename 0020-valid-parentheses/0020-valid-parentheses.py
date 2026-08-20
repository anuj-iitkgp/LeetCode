class Solution(object):
    def isValid(self, s):
        n = len(s)
        stack = []

        for i in range(n):
            if s[i] == "(" or s[i] == "[" or s[i] == "{":
                stack.append(s[i])
            else:
                if len(stack) == 0:
                    return False
                char = stack[-1]
                stack.pop()

                if not ((s[i] == ")" and char == "(") or (s[i] == "]" and char == "[") or (s[i] == "}" and char == "{")):
                    return False
        return len(stack) == 0

# Time and Space Complexity: O(n)
