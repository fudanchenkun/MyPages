import sys

class Solution(object):
    def splitArray(self, nums, m):
        length = len(nums)
        d = []
        for i in range(length):
            tmp = [0] * (length+1)
            for j in range(i+1, length+1):
                tmp[j] = sum(nums[i:j])
            d.append(tmp)

        def findGroup(l, c):
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
        ans = sys.maxint #d[0][length]
        for line in lines:
            max_line = 0
            start = 0
            for i in line:
                s = d[start][i] # sum(nums[start:i])
                if s > max_line:
                    max_line = s
                start = i
            max_line = max(max_line, d[start][length]) #sum(nums[start:]))#
            if max_line < ans:
                ans = max_line
        return ans

class binarySearchSolution(object):
    def splitArray(self, nums, m):
        length = len(nums)
        def countGroup(mid):
            s = 0
            count = 0
            max_s = 0
            for i in range(length):
                s += nums[i]
                if s > mid:
                    s = nums[i]
                    count += 1
                    if count > m:
                        return count
            return count + 1
        left = max(nums)
        right = sum(nums)
        while left < right:
            mid = (left + right) / 2
            c = countGroup(mid)
            if c > m:
                left = mid + 1
            else:
                right = mid
        return left
