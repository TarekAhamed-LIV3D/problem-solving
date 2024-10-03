from collections import defaultdict
from typing import List

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        rc = defaultdict(int)
        cc = defaultdict(int)
        for row in grid:
            rc[tuple(row)] += 1
        for col in range(n):
            cc[tuple(grid[i][col] for i in range(n))] += 1
        ans = 0
        for row, count in rc.items():
            ans += count * cc[row]
        return ans

grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]
Solution = Solution()
ans = Solution.equalPairs(grid)
print(ans)