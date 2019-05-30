class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        import copy
        if len(nums) <=2:
            return []
        if len(nums) == 3:
            return [nums] if sum(nums) == 0 else []
        triplets=[]
        pre_list_set = set()
        def findTriplets(pre_nums,sub_nums):
            pre_tuple = tuple(pre_nums)
            if pre_tuple in pre_list_set:
                return
            pre_list_set.add(pre_tuple)
            if len(pre_nums) == 2:
                sum_pre_nums = sum(pre_nums)
                for num in sub_nums:
                    if num + sum_pre_nums == 0:
                        tmp = copy.copy(pre_nums)
                        tmp.append(num)
                        triplets.append(tuple(tmp))
                return
            for i in range(len(sub_nums)-1):
                tmp = copy.copy(pre_nums)
                tmp.append(sub_nums[i])
                findTriplets(tmp, sub_nums[i+1:])
        findTriplets([], nums)
        return list(set(triplets))