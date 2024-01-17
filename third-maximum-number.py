def thirdMax(nums):
    unique_nums = list(set(nums))
    unique_nums.sort(reverse=True)

    if len(unique_nums) >= 3:
        return unique_nums[2]
    else:
        return unique_nums[0]

nums = [2, 2, 3, 1]
result = thirdMax(nums)

print(f"The third distinct maximum number is: {result}")