class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        target = {}
        window = {}

        if len(s1) > len(s2):
            return False

        for ch in s1:
            target[ch] = target.get(ch, 0) + 1

        left = 0 

        for right in range(len(s2)):
            window[s2[right]] = window.get(s2[right], 0) + 1

            if right - left + 1 > len(s1):
                window[s2[left]] -= 1

                if window[s2[left]] == 0:
                    del window[s2[left]]

                left += 1

            if window == target: 
                return True

        return False  