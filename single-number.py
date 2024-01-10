from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            result ^= num
        return result

input_array = [2, 2, 1]

solution = Solution()
result = solution.singleNumber(input_array)

print("Single number:", result)
