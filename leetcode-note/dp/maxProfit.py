"""
关键是状态转移方程，dp[i]表示第i天买入的最大利润
第i天买入的最大利润，可能是第i+1天买入的最大利润与第i天价格和第i+1天价格的差值之和，或者可能就是这个差值（即第i天买入，i+1天卖出），取较大值即可
相当于，dp[i+1]保存了第i+2天以后卖出的利润的最大值，这样只要再和第i+1卖出得到的利润比较即可
"""

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        length = len(prices)
        if length <= 1:
            return 0
        dp = [0] * length
        for i in range(length-2, -1 , -1):
            tmp = prices[i+1] - prices[i]
            dp[i] = max(dp[i+1] + tmp, tmp)
        return max(dp)