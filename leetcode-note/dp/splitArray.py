import sys

class Solution(object):
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        length = len(nums)
        dp = []
        for i in range(length):
            tmp = [0] * (length+1)
            for j in range(i+1, length+1):
                tmp[j] = sum(nums[i:j])
            # print tmp
            dp.append(tmp)

        def findGroup(l, c):
            # print c
            if c == 0:
                return []
            if c == 1:
                return [[e] for e in l]
            r = []
            for i in range(len(l)):
                for e in findGroup(l[i+1:], c - 1):
                    r.append([l[i]] + e)
            return r

        lines = findGroup(range(1, length) , m-1)
        ans = sys.maxint#dp[0][length]
        for line in lines:
            # print line
            max_line = 0
            start = 0
            for i in line:
                s = dp[start][i]# sum(nums[start:i])
                if s > max_line:
                    max_line = s
                start = i
            max_line = max(max_line, dp[start][length]) #sum(nums[start:]))#
            # print max_line
            if max_line < ans:
                ans = max_line
        return ans