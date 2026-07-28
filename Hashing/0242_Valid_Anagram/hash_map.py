class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        if len(s) != len(t):
            return False

        freqS = {}
        freqT = {} 

        for ch in s:
            if ch in freqS:
                freqS[ch] += 1
            else:
                freqS[ch] = 1

        for ch in t:
            if ch in freqT:
                freqT[ch] += 1
            else:
                freqT[ch] = 1

        return freqS == freqT 