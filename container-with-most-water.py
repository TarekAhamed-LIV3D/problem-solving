from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        mx = 0 
        while l < r:
            area = (r - l) * min(height[l], height[r])
            mx = max(mx, area)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1 
        return mx
        
height = [1,8,6,2,5,4,8,3,7]
Solution =  Solution()
ans =  Solution.maxArea(height)
print(ans)