class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        stack = []
        greater = {}

        for num in nums2:
            while stack and num > stack[-1]:
                smaller = stack.pop()
                greater[smaller] = num

            stack.append(num)

        ans = []

        for num in nums1:
            ans.append(greater.get(num, -1))

        return ans