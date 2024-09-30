from typing import List

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        m, r, l, c =  0, 0, 0, 0
        x = len(nums)
        for r in range(x):
            if nums[r] == 0:
                c += 1
            while c > 1:
                if nums[l] == 0:
                    c -= 1
                l += 1
            m = max(m, r - l)
        if m != x:
            return m
        else:
            return m - 1
        
nums = [0,1,1,1,0,1,1,0,1]
Solution = Solution()
ans =  Solution.longestSubarray(nums)
print(ans)