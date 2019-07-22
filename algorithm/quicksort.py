def quicksort(nums, r, l):

    if r >= l:
        return

    i = r
    j = l
    flag = nums[r]

    while i < j:
        while nums[j] >= flag and i < j:
            j -= 1
        if i < j:
            nums[i] = nums[j]
            i += 1

        while nums[i] < flag and i < j:
            i += 1
        if i < j:
            nums[j] = nums[i]
            j -= 1
    # print(flag, i)
    nums[i] = flag
    quicksort(nums, r, i-1)
    quicksort(nums, i+1, l)
    # print("out", nums)


if __name__ == '__main__':
    test = [13,8,7,9,15,14,12,15]
    quicksort(test, 0, len(test) -1)
    print(test)




