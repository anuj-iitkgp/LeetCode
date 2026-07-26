class Solution(object):
    def longestValidParentheses(self, s):
        stack = [-1]
        max_len = 0

        for i, char in enumerate(s):
            if char == "(":
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    max_len = max(max_len, i - stack[-1])
        return max_len


"""
**Initialization:** Create a stack with `[-1]` as the initial base boundary for calculating substring lengths from index `0`, and set `max_len = 0`.
* **Traverse String:** Loop through each character `char` at index `i` in string `s`.
* **Push `('`:** If `char == '('`, push its index `i` onto the stack.
* **Process `)'`:** If `char == ')'`, pop the top index from the stack.
* **New Boundary:** If the stack becomes empty after popping, push the current index `i` onto the stack as the new boundary.
* **Calculate Length:** If the stack is not empty, calculate the valid substring length as `i - stack[-1]` and update `max_len = max(max_len, i - stack[-1])`.


* **Return Result:** Return `max_len` after processing all characters in the string.
* **Complexity:** Runs in **$O(n)$ time** (single pass) and uses **$O(n)$ space** (stack memory).  

"""