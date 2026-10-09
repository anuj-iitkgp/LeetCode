class Solution(object):
    def removeDigit(self, number, digit):
        r, n = 0, len(number)
        for i in range(len(number)):
            if number[i] == digit:
                r = i
                if i + 1 < n and int(number[i + 1]) > int(number[i]):
                    return number[0:i] + number[i+1:]
        
        return number[0:r] + number[r + 1:]
