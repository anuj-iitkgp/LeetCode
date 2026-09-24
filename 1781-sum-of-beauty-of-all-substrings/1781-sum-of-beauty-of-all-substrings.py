from collections import Counter
class Solution(object):
    def beautySum(self, s):
        n = len(s)
        t = 0
        for i in range(n):
            count = Counter()
            for j in range(i, n):
                count[s[j]] += 1
                a = max(count.values())
                b = min(count.values())
                t += (a - b)
        return t
        
        

# from collections import Counter
# class Solution(object):
#     def beautySum(self, s):
#         n = len(s)
#         t = 0
#         for i in range(n):
#             for j in range(i, n):
#                 count = Counter(s[i:j+1])
#                 a = max(count.values())
#                 b = min(count.values())
#                 t += (a - b)
#         return t
        
        