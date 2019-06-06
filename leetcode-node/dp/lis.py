

def lis(nums):
    dp = [[]] * len(nums)
    print(dp)
    dp[0] = [nums[0]]
    for i in range(len(nums)): # 状态总数
        for j in range(i): # 每个状态的决策个数
            if nums[j] < nums[i]: # 决策时间
                dp[i] = dp[j].copy() + [nums[i]]
    # return max(dp, key=lambda y: len(y))
    print(dp)

if __name__ == '__main__':
    nums = [1, 6, 2, 3, 7, 5]
    print(lis(nums))
