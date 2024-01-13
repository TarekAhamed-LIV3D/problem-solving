class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        candidate = None
        count = 0

        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)

        return candidate

nums = [2, 2, 1, 1, 1, 2, 2]
solution = Solution()
result = solution.majorityElement(nums)

print("Majority element:", result)
