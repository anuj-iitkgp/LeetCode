class Solution(object):
    def firstPalindrome(self, words):
        ans = ""
        for word in words:
            if word == word[::-1]:
                ans += word
                break
        return ans