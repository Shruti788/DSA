class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums2_set = set(nums2)
        result = set()

        for num in nums1:
            if num in nums2_set:
                result.add(num)

        return list(result)  