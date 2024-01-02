def searchInsert(nums, target):
    low, high = 0, len(nums) - 1
    
    while low <= high:
        mid = (low + high) // 2
        
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return low

sorted_array = [1, 3, 5, 6]
target_value = 5

result = searchInsert(sorted_array, target_value)
print("Index of", target_value, "or where it should be inserted:", result)
