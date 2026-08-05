class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        mapST = {}
        mapTS = {}

        for i in range(len(s)):

            charS = s[i]
            charT = t[i]

            if charS in mapST:
                if mapST[charS] != charT:
                    return False
            else:
                mapST[charS] = charT

            if charT in mapTS:
                if mapTS[charT] != charS:
                    return False
            else:
                mapTS[charT] = charS

        return True