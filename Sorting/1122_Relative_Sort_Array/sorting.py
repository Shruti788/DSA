class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        count = {}

        for num in arr1:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1

        result = []

        for num in arr2:
            for _ in range(count[num]):
                result.append(num)

        remaining = []

        for num in count:
            if num not in arr2:
                for _ in range(count[num]):
                    remaining.append(num)

        remaining.sort()
        result.extend(remaining)

        return result  