class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        n = len(bills)
        five = 0
        ten = 0

        for i in range(0, n):
            if bills[i] == 5:
                five += 1

            elif bills[i] == 10:
                if five == 0:
                    return False 

                five -= 1
                ten += 1    
                         
            elif bills[i] == 20:
                if five > 0 and ten > 0:
                    five -= 1
                    ten -= 1
                elif five >= 3:
                    five -= 3
                else:
                    return False

        return True   