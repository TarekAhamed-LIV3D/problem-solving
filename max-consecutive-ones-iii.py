from typing import List

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        m1, z, l = 0, 0, 0  
        for r in range(len(nums)):
            if nums[r] == 0:
                z += 1
            while z > k:
                if nums[l] == 0:
                    z -= 1
                l += 1
            m1 = max(m1, r - l + 1)
        return m1

Solution = Solution()
nums = [1,1,1,0,0,0,1,1,1,1,0]
k = 2
ans = Solution.longestOnes(nums, k)
print(ans)