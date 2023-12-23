def twoSum(nums: list[int], target: int) -> list[int]:
    complement_dict = {}

    for i, num in enumerate(nums):
        complement = target - num
        if complement in complement_dict:
            return [complement_dict[complement], i]
        complement_dict[num] = i
    return None

nums = [2, 7, 11, 15]
target = 9
result = twoSum(nums, target)
print(result)