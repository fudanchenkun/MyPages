---
layout: post
title:  "3sum问题"
date:   2019-05-31 20:54:56
categories: jekyll update
---


## 3sum


```
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.
Note:
The solution set must not contain duplicate triplets.
Example:
Given array nums = [-1, 0, 1, 2, -1, -4],
A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
```

开始以为是排列组合问题，用递归写了一个通用的方法：
1. 找出所有的三元组
2. 计算每个三元组和是否是0（target）
3. 三元组列表去重
```python
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
```

有如下问题：
+ 遍历了所有三元组的可能性，时间复杂度高
+ 每次递归都要给列表添加元素，对于python的可变类型list和引用传递的关系，都必须复制一个list
+ 无法在递归调用中对重复的三元组去重，只能把符合条件的三元组放入一个list，最后去重，正由于要去重，每个三元组
还要存成tuple（tuple是可哈希的，list不是）

其实本题是基于2sum问题，首先对数组排序，3sum需要设置first指针指向第一个数，然后像2sum问题那样设置两个指针，left指向
first后第一个数，right指向数组最后一个数，然后根据sum和target的差值移动left和right。除了这个思路之外，本题难点
还在于：
> 数组里的数是有重复的，要考虑去重问题，不能直接set(list)去重，去重针对三个指针，跳过相同的数字

代码如下
```python
"""
判断nums[c]最小的数 因此后面的累加和一定大于4 * nums[c]
要充分利用有序数列的特点，写出不等式，搜小范围
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
                        while left < right and nums[left] == nums[left-1]: #去重
                            left += 1
                        right -= 1
                        while left < right and nums[right] == nums[right+1]: #去重
                            right -= 1
                    elif diff < 0:
                        left += 1
                    else:
                        right -= 1
                i += 1
                while i < nums_len and nums[i-1] == nums[i]: #去重
                    i += 1
            c += 1
            while c < nums_len and nums[c-1] == nums[c]:
                c += 1
        return triplets
```



还有两个变种，如下
- 差值改为绝对值 [3sum Closest](https://leetcode.com/problems/3sum-closest/)
- 增加复杂度 [4sum](https://leetcode.com/problems/4sum/)

## 总结
> 这道题解题思路很常见，我觉得更值得注意的是利用了有序数列的特点处理去重问题。剪枝缩小范围在算法占据了
很重要的位置。







 
 


