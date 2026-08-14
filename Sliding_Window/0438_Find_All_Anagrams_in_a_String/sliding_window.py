class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        target = {}
        window = {}
        result = []

        if len(p) > len(s):
            return result

        for ch in p:
            target[ch] = target.get(ch, 0) + 1

        left = 0        

        for right in range(len(s)):
            window[s[right]] = window.get(s[right], 0) + 1

            if right - left + 1 > len(p):
                window[s[left]] -= 1
                
                if window[s[left]] == 0:
                    del window[s[left]]  

                left += 1 

            if window == target:
                result.append(left)

        return result 