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
            return abs(sum(nums) - target)
        nums_len = len(nums)
        i = 0
        nums.sort()
        sum_min = sum(nums[:3])
        sum_max = sum(nums[-3:])
        if target >= sum_max:
            return target - sum_max
        elif target <= sum_min:
            return sum_min - target
        diff_max = max([sum_max - target, target - sum_min])

        while i < nums_len - 2 and nums[i] <= target:
            #print diff_max
            left = i + 1
            right = nums_len - 1
            while left < right:
                diff = nums[i] + nums[left] + nums[right] - target
                # print nums[i], nums[left], nums[right]
                if diff == 0:
                    return 0
                elif diff < 0:
                    diff = 0 - diff
                    if diff < diff_max:
                        diff_max = diff
                    left += 1
                else:
                    if diff < diff_max:
                        diff_max = diff
                    right -= 1
            i += 1
            while i < nums_len and nums[i-1] == nums[i]:
                i += 1
        return diff_max