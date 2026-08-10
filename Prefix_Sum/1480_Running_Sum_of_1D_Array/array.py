class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        ans = [0] * n

        ans[0] = nums[0]

        for i in range(1, n):
            ans[i] = ans[i-1] + nums[i]

        return ans  