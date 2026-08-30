class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []

        matches = {
            ')' : '(',
            ']' : '[',
            '}' : '{'
        }

        for char in s:
            if char in matches:
                if not stack or stack[-1] != matches[char]:
                    return False

                stack.pop()

            else:
                stack.append(char)

        return len(stack) == 0 