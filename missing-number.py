class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n = len(nums)
        expected_sum = n * (n + 1) // 2
        actual_sum = sum(nums)
        return expected_sum - actual_sum

nums = [3, 0, 1]
solution = Solution()
result = solution.missingNumber(nums)

print(f"The missing number is: {result}")