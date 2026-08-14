class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
        count = {}
        left = 0
        max_length = 0

        for right in range(len(fruits)):
            if fruits[right] in count:
                count[fruits[right]] += 1
            else:
                count[fruits[right]] = 1   

            while len(count) > 2:
                count[fruits[left]] -= 1

                if count[fruits[left]] == 0:
                    del count[fruits[left]] 

                left += 1

            max_length = max(max_length, right - left + 1)  

        return max_length    