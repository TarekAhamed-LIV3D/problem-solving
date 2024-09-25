from typing import List

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = second = float('inf')
        for i in nums:
            if i <= first:
                first = i
            elif i <= second:
                second = i
            else:
                return True
        return False

nums = [5,4,3,2,1]
solution = Solution()
result = solution.increasingTriplet(nums)
print(result)