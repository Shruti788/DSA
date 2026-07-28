class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
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

        for key, value in freqT.items():
            if key not in freqS:
                return key

            if freqS[key] != value: 
                return key 