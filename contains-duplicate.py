class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        seen = set()

        for num in nums:
            if num in seen:
                return True
            seen.add(num)

        return False

nums = [1, 2, 3, 1]
solution = Solution()
result = solution.containsDuplicate(nums)

print(f"Contains duplicate values: {result}")