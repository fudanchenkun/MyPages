class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        length = len(height)
        ans = 0
        for i in range(length - 1):
            tmp = 0
            for j in range(i+1, length):
                tmp = max(tmp, min(height[i], height[j]) * (j - i))
            ans = max(tmp, ans)
        return ans