class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        left = 0
        right = 0 
        result = []

        while left < len(word1) and right < len(word2):
            result.append(word1[left])
            left += 1

            result.append(word2[right])
            right += 1

        while left < len(word1):
            result.append(word1[left])
            left += 1

        while right < len(word2):
            result.append(word2[right])  
            right += 1

        return "".join(result)     