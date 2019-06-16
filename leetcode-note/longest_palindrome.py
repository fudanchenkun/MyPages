class DPSolution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        length = len(s)
        if length <= 1:
            return s
        dp = []
        for i in range(length):
            dp.append([None] * length)
        # 初始化1个字母和2个字母的回文
        for i in range(length - 1):
            dp[i][i] = s[i]
            if s[i] == s[i+1]:
                dp[i][i+1] = s[i] + s[i+1]
        dp[length-1][length-1] = s[length-1]

        def isPalindrome(start, end):
            if start == end:
                return True
            if start + 1 == end:
                return not dp[start][end] is None
            if s[start] == s[end]:
                return isPalindrome(start+1,end-1)
            else:
                return False

        longest = 1
        ans = s[0]
        for i in range(length-1):
            for j in range(i+1,length):
                if isPalindrome(i, j):
                    dp[i][j] = s[i:j+1]
                    if j - i + 1 > longest:
                        longest = j - i + 1
                        ans = dp[i][j]
        return ans


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        length = len(s)
        if length <= 1:
            return s
        longest = 1
        ans = s[0]
        if s[0] == s[1]:
            longest = 2
            ans = s[0:2]
        for i in range(1, length-1):
            for j in [i-1,i]:
                start = j
                end = i+1
                while start >= 0 and end <= length-1:
                    if s[start] == s[end]:
                        start -= 1
                        end += 1
                    else:
                        break
                tmp = end - start - 1
                if tmp > longest:
                    longest = tmp
                    ans = s[start + 1:end]
        return ans