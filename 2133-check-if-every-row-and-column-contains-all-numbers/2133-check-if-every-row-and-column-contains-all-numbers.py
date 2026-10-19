# from collections import Counter
# class Solution(object):
#     def checkValid(self, matrix):
#         transposed = list(map(list, zip(*matrix)))
#         n = len(transposed)
#         count = []
#         for i in range(n):
#             count += transposed[i]
#         count1 = Counter(count)
#         print(count1)

#         for val in count1.values():
#             if val != n:
#                 return False
#         return True

# from collections import Counter
# class Solution(object):
#     def checkValid(self, matrix):
#         transpose = list(map(list, zip(*matrix)))
#         n, m = len(matrix), len(transpose)
#         sum1 = n * (n + 1) // 2
#         sum2 = m * (m + 1) // 2
#         for i in range(n):
#             if sum1 != sum(matrix[i]) or sum2 != sum(transpose[i]):
#                 return False
#         return True

class Solution(object):
    def checkValid(self, matrix):
        n = len(matrix)
        target = set(range(1, n + 1))

        for row in matrix:
            if set(row) != target:
                return False
            
        for col in zip(*matrix):
            if set(col) != target:
                return False
        return True

        




# from collections import Counter
# class Solution(object):
#     def checkValid(self, matrix):
#         transposed = list(map(list, zip(*matrix)))
#         n = len(matrix)
#         for i in range(n):
#             count = Counter(matrix[i])
#             for val in count.values():
#                 if val != 1:
#                     return False
#         return True
        