# from collections import Counter
# class Solution(object):
#     def relativeSortArray(self, arr1, arr2):
#         count = Counter(arr1)
#         ans = []
#         for i in range(len(arr2)):
#             if arr2[i] in count:
#                 for j in range(count[arr2[i]]):
#                     ans.append(arr2[i])
#         count1 = Counter(ans)
#         n = len(arr1)
#         ans1 = []
#         for i in range(n):
#             if arr1[i] not in count1:
#                 ans1.append(arr1[i])
#         ans1.sort()
#         k = len(ans1)
#         for i in range(k):
#             ans.append(ans1[i])
#         return ans


from collections import Counter

class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        count = Counter(arr1)
        ans = []
        
        # Add elements of arr2 in relative order
        for x in arr2:
            ans.extend([x] * count.pop(x))
            
        # Add remaining elements in ascending order
        for x in sorted(count.keys()):
            ans.extend([x] * count[x])
            
        return ans
        