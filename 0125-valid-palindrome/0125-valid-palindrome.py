class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        word = "".join(c for c in s if c.isalnum())
        word1 = word.lower()
        return word1 == word1[::-1]