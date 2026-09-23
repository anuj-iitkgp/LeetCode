class Solution(object):
    def findPrimePairs(self, n):
        is_prime = [True] * (n + 1)
        is_prime[0] = is_prime[1] = False
        
        for i in range(2, int(n**0.5) + 1):
            if is_prime[i]:
                for j in range(i * i, n + 1, i):
                    is_prime[j] = False

        ans = []
        for x in range(2, (n // 2) + 1):
            if is_prime[x] and is_prime[n - x]:
                ans.append([x, n - x])

        return ans
        for i in range(2, n):
            if isPrime(i) and isPrime(n - i) and i <= n - i and n - i <= n :
                ans.append([i, n - i])
        return ans
            
            
        
        
            



        









# class Solution(object):
#     def findPrimePairs(self, n):
#         def isPrime(n):
#             if n <= 1:
#                 return False
#             for i in range(2, int(n**(0.5)) + 1):
#                 if n % i == 0:
#                     return False
#             return True

#         primes = set()
#         for i in range(2, n + 1):
#             if isPrime(i):
#                 primes.add(i)
#         ans = []
#         m = len(primes)
#         for i in range(2, n):
#             if i in primes and n - i in primes:
#                 ans.append([i, n - i])
#                 primes.remove(i)
#         return ans
            
            
        
        
            



        