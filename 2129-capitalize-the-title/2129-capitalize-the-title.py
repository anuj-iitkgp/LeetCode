class Solution(object):
    def capitalizeTitle(self, title):
        """
        :type title: str
        :rtype: str
        """
        # return " ".join(word.capitalize() for word in title.split() if len(word) > 2)
        res = ""
        for word in title.split():
            if len(word) <= 2:
                res += " " + word.lower() 
            elif len(word) > 2:
                res += " "  + word.lower().capitalize()
        return res[1:]
        