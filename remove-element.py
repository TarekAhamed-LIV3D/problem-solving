def removeElement(nums, val):
    if not nums:
        return 0

    non_val_pointer = 0

    for i in range(len(nums)):
        if nums[i] != val:
            nums[non_val_pointer] = nums[i]
            non_val_pointer += 1

    return non_val_pointer

nums = [3, 2, 2, 3, 4, 5, 3]
val = 3
k = removeElement(nums, val)

print(nums[:k])
print("Number of elements not equal to", val, ":", k)
