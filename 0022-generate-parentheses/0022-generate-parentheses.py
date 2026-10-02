class Solution(object):
    def generateParenthesis(self, n):
        ans = []

        def backtrack(open_count, close_count, curr):
            
            if len(curr) == 2 * n:
                ans.append(curr)
                return 
            
            if open_count < n:
                backtrack(open_count + 1, close_count, curr + "(")
            
            if close_count < open_count:
                backtrack(open_count, close_count + 1, curr + ")")
        
        backtrack(0, 0, "")
        return ans