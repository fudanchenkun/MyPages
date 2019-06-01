class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        def match(s, value):
            if s == '(' and value == ')':
                return True
            if s == '[' and value == ']':
                return True
            if s == '{' and value == '}':
                return True
            return False
        stack = []
        for i in range(len(s)):
            if len(stack) == 0:
                stack.append(s[i])
                continue
            if match(stack[-1], s[i]):
                stack.pop()
            else:
                stack.append(s[i])
        if len(stack) == 0:
            return True
        return False