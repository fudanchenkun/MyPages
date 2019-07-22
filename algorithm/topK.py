def topK(nums, k):

    def partition(tmpk, left, right):
        # print(nums)
        if left > right:
            return
        if left == right:
            return nums[left]
        i = left
        j = right
        flag = nums[left]
        while i < j:
            while i < j and nums[i] <= flag:
                i += 1
            if i < j:
                nums[j] = nums[i]
                j -= 1

            while i < j and nums[j] > flag:
                j -= 1
            if i < j:
                nums[i] = nums[j]
                i += 1
        nums[i] = flag
        tmp = i - left + 1
        # print(i)
        if tmp == tmpk:
            print("i:",i)
            return nums[i]
        if tmp < tmpk:
            return partition(tmpk - tmp, i+1, right)
        else:
            return partition(tmp - tmpk, left, i-1)
    return partition(k, 0, len(nums) - 1)
    # return nums[:k]

import random
if __name__ == '__main__':
    nums = [random.randint(1, 100) for i in range(10)]
    k = 3
    print(topK(nums, k))
    print(nums)
    nums.sort()
    print(nums[k])


