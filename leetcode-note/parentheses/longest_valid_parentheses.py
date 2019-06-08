class Solution(object):
    def dpLongestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        dp = [0] * (len(s) + 1)
        stack = []
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            elif stack:
                j = stack.pop()
                dp[i+1] = dp[j] + (i - j + 1)

        for i in range(len(s)):
            print(s[i], dp[i+1])
        return  max(dp)


    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
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
                stack.append([i, s[i]])
                continue
            if match(stack[-1][1], s[i]):
                stack.pop()
            else:
                stack.append([i, s[i]])
        stack_len = len(stack)
        max_len = 0
        if len(stack) == 0:
            return len(s)
        else:
            if stack[0][0] > 0:
                max_len = stack[0][0]
            if stack[-1][0] < len(s) - 1:
                tmp = len(s) - 1 - stack[-1][0]
                if tmp > max_len:
                    max_len = tmp

        for i in range(stack_len - 1):
            tmp = stack[i+1][0] - stack[i][0] - 1
            if tmp > max_len:
                max_len = tmp

        return max_len

def stringToString(input):
    return input[1:-1].decode('string_escape')

def intToString(input):
    if input is None:
        input = 0
    return str(input)

def main():
    import sys
    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')
    lines = readlines()
    while True:
        try:
            line = lines.next()
            s = stringToString(line)

            ret = Solution().longestValidParentheses(s)

            out = intToString(ret)
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()