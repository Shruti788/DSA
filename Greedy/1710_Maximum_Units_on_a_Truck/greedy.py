class Solution(object):
    def maximumUnits(self, boxTypes, truckSize):
        """
        :type boxTypes: List[List[int]]
        :type truckSize: int
        :rtype: int
        """
        boxTypes.sort(key=lambda x: x[1], reverse=True)
        total_units = 0

        for boxType in boxTypes:
            boxes = min(boxType[0], truckSize)

            total_units += boxes * boxType[1]
            truckSize -= boxes

            if truckSize == 0:
                break
                
        return total_units  