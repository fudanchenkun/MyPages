class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) <=2:
            return -1
        if len(nums) == 3:
            return sum(nums)
        nums_len = len(nums)
        i = 0
        nums.sort()
        sum_min = sum(nums[:3])
        sum_max = sum(nums[-3:])
        if target >= sum_max:
            # print "max"
            return

        if  target <= sum_min:
            # print "min"
            return sum_min
        diff_max = max([sum_max - target, target - sum_min])
        ans = 0
        while i < nums_len - 2:
            # 由于是求绝对值最小，暂时无法推测3nums[i]与target的差值
            left = i + 1
            right = nums_len - 1
            while left < right:
                tmp = nums[i] + nums[left] + nums[right]
                # print tmp
                diff = tmp - target
                if diff == 0:
                    return tmp
                elif diff < 0:
                    diff = 0 - diff
                    if diff < diff_max:
                        diff_max = diff
                        ans = tmp
                    left += 1
                else:
                    if diff < diff_max:
                        diff_max = diff
                        ans = tmp
                    right -= 1
            i += 1
            # while i < nums_len and nums[i-1] == nums[i]:
            #     i += 1
        return ans