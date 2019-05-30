class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        target = 0
        nums.sort()
        if len(nums) <=2:
            return []
        if len(nums) == 3:
            return [nums] if sum(nums) == target else []
        triplets=[]
        nums_len = len(nums)
        i = 0
        while i < nums_len - 2 and nums[i] <= target:
            left = i + 1
            right = nums_len - 1


            while left < right:
                diff = nums[i] + nums[left] + nums[right] - target
                # print nums[i], nums[left], nums[right]
                if diff == 0:
                    triplets.append([nums[i], nums[left], nums[right]])
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
        return triplets