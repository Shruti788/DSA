class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        intervals.sort(key=lambda x: x[1])
        count = 0
        end_point = intervals[0][1]

        for i in range(1, len(intervals)):
            if intervals[i][0] < end_point:
                count += 1
            else:
                end_point = intervals[i][1]

        return count  