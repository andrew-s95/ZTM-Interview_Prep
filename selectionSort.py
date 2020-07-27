def selectionSort(nums):
    i = 0
    while i < len(nums):
        min = nums[i]
        index = index
        for j in range(i+1, len(nums)):
            if nums[j] < min:
                index = j
                min = nums[j]
        nums[i], nums[index] = nums[index], nums[i]
        i += 1
    return nums

print(selectionSort([1,4,2,6,3,7,9]))