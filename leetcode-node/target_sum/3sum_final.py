"""
判断nums[c]最小的数 因此后面的累加和一定大于4 * nums[c]
要充分利用有序数列的特点，写出一点不等式
"""

class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        c = 0
        nums_len = len(nums)
        if len(nums) <=3:
            return []
        if len(nums) == 4:
            return [nums] if sum(nums) == target else []
        triplets=[]
        while c < nums_len - 3 and nums[c] <= (target/4): #
            i = c + 1
            target_3 = target - nums[c]
            while i < nums_len - 2 and nums[i] <= (target_3/3): #
                left = i + 1
                right = nums_len - 1
                while left < right:
                    diff = nums[i] + nums[left] + nums[right] - target_3
                    # print nums[c], nums[i], nums[left], nums[right]
                    if diff == 0:
                        triplets.append([nums[c], nums[i], nums[left], nums[right]])
                        left += 1
                        while left < right and nums[left] == nums[left-1]:
                            left += 1
                        right -= 1
                        while left < right and nums[right] == nums[right+1]:
                            right -= 1
                    elif diff < 0:
                        left += 1
                    else:
                        right -= 1
                i += 1
                while i < nums_len and nums[i-1] == nums[i]:
                    i += 1
            c += 1
            while c < nums_len and nums[c-1] == nums[c]:
                c += 1

        return triplets