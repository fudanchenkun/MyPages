class DPSolution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = len(s)
        if length <= 1:
            return length
        dp = [""] * length
        dp[0] = s[0]
        i = 1
        ans = 1
        while i < length:
            if dp[i-1] in s[i]:
                dp[i] = dp[i-1] + s[i]
                if len(dp[i]) > ans:
                    ans = len(dp[i])
            else:
                tmp = i - len(dp[i-1]) + dp[i-1].index(s[i])
                dp[i] = s[tmp + 1:i+1]
            i += 1
        return ans

class MapSWSolution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = len(s)
        if length <= 1:
            return length
        m = {}
        for i in range(length):
            if not s[i] in m:
                m[s[i]] = []
            m[s[i]].append(i)
        left = 0
        right = 0
        ans = 1
        i = 1
        while i < length:
            tt = -1
            for each in m[s[i]]:
                if each >= left and each <= right:
                    tt = each
                    break
            if tt != -1:
                left = tt + 1
            right = i
            tmp = right - left + 1
            ans = tmp if tmp > ans else ans
            i += 1
        return ans


class SWSolution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = len(s)
        if length <= 1:
            return length

        left = 0
        right = 0
        ans = 1
        i = 1
        while i < length:
            j = right
            while j >= left:
                if s[i] == s[j]:
                    left = j + 1
                    break
                else:
                    j -= 1
            right = i
            tmp = right - left + 1
            ans = tmp if tmp > ans else ans
            i += 1
        return ans

class DPMapSolution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = len(s)
        if length <= 1:
            return length
        dp = [{} for i in range(length)]

        dp[0] = {s[0]:0}
        i = 1
        ans = 1
        while i < length:
            if not s[i] in dp[i-1]:
                dp[i] = dp[i-1]
                dp[i][s[i]] = i
                if len(dp[i]) > ans:
                    ans = len(dp[i])
            else:
                tmp = dp[i-1][s[i]]
                for j in range(tmp+1, i+1):
                    dp[i][s[j]] = j
            i += 1

        return ans

class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        st = {}
        i, ans = 0, 0
        for j in range(len(s)):
            if s[j] in st:
                i = max(st[s[j]], i)
            ans = max(ans, j - i + 1)
            st[s[j]] = j + 1
        return ans