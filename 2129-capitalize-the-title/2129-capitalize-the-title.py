class Solution(object):
    def capitalizeTitle(self, title):
        """
        :type title: str
        :rtype: str
        """

        return " ".join(word.lower() if len(word) <= 2 else word.capitalize() for word in title.split() )

        #-- brute force--
        # res = ""
        # for word in title.split():
        #     if len(word) <= 2:
        #         res += " " + word.lower() 
        #     elif len(word) > 2:
        #         res += " "  + word.lower().capitalize()
        # return res[1:]
        