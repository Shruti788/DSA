class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """ 
        count = 0
        prefix = 0
        freq = {0: 1}

        for num in nums:
            prefix += num

            needed = prefix - k

            if needed in freq:
                count += freq[needed]

            freq[prefix] = freq.get(prefix, 0) + 1

        return count 