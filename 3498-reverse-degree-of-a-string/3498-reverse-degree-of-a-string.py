class Solution(object):
    def reverseDegree(self, s):
        return sum(i * (123 - ord(char)) for i, char in enumerate(s, start=1))


        
        # reversed_dict = {char: 26 - i for i, char in enumerate(string.ascii_lowercase)}
        # return sum(i * reversed_dict[char] for i, char in enumerate(s, start=1))

        # n = len(s)
        # ans = 0
        # for i in range(1, n + 1):
        #     ans += i * reversed_dict[s[i - 1]]
        # return ans






            

        