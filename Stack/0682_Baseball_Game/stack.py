class Solution(object):
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        stack = []

        for op in operations:
            if op not in ['C', 'D', '+']:
                stack.append(int(op))

            elif op == 'C':
                stack.pop()

            elif op == 'D':
                stack.append(stack[-1] * 2) 

            elif op == '+':
                stack.append(stack[-1] + stack[-2])

        return sum(stack) 