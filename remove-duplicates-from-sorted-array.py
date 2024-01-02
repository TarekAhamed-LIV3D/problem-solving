def removeDuplicates(nums):
    if not nums:
        return 0
    unique_pointer = 0

    for i in range(1, len(nums)):
        if nums[i] != nums[unique_pointer]:
            unique_pointer += 1
            nums[unique_pointer] = nums[i]
    return unique_pointer + 1

nums = [1, 1, 2, 2, 2, 3, 4, 4, 5]
k = removeDuplicates(nums)

print(nums[:k])
print("Number of unique elements:", k)
