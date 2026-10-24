import itertools

class Solution:
    def countAndSay(self, n: int) -> str:
        res = "1"
        
        for _ in range(n - 1):
            # groupby groups consecutive identical characters
            # e.g., "1121" -> ('1', ['1', '1']), ('2', ['2']), ('1', ['1'])
            res = "".join(str(len(list(group))) + digit for digit, group in itertools.groupby(res))
            
        return res

        