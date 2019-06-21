"""
要求在log(n)内实现，立刻反应出要用二分查找
分完以后，发现必然有一边是正常排序，而另一边则必定是一个转换数组
这样就可以在二分查找的过程中，嵌入递归，解决子问题
"""


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        length = len(nums)
        if length == 0:
            return -1
        low = 0
        high = length - 1

        def subSearch(lo, hi):
            if lo == hi:
                return lo if nums[lo] == target else -1
            while lo < hi:
                mid = (lo + hi)/2
                if nums[mid] == target:
                    return mid
                if nums[lo] <= nums[mid]:
                    if target < nums[mid] and target >= nums[lo]:
                        hi = mid - 1
                    else:
                        return subSearch(mid+1,hi)
                else:
                    if target > nums[mid] and target <= nums[hi]:
                        lo = mid + 1
                    else:
                        return subSearch(lo, mid-1)
            if nums[lo] == target:
                return lo
            elif nums[hi] == target:
                return hi
            return -1
        return subSearch(low, high)
