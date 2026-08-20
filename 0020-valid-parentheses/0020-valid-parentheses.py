# class Solution(object):
#     def isValid(self, s):
#         n = len(s)
#         stack = []

#         for i in range(n):
#             if s[i] == "(" or s[i] == "[" or s[i] == "{":
#                 stack.append(s[i])
#             else:
#                 if len(stack) == 0:
#                     return False
#                 char = stack[-1]
#                 stack.pop()

#                 if not ((s[i] == ")" and char == "(") or (s[i] == "]" and char == "[") or (s[i] == "}" and char == "{")):
#                     return False
#         return len(stack) == 0

class Solution(object):
    def isValid(self, s):
        stack = []
        
        # Map matching closing brackets to opening brackets
        mapping = {")": "(", "]": "[", "}": "{"}

        for char in s:
            if char in mapping:
                # Pop from stack if non-empty, otherwise assign a dummy value
                top_element = stack.pop() if stack else '#'
                if mapping[char] != top_element:
                    return False
            else:
                stack.append(char)

        return len(stack) == 0

# Time Complexity: O(n)
# Space Complexity: O(n)

# Time and Space Complexity: O(n)
