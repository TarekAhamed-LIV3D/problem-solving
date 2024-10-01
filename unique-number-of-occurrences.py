from typing import List

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        c = {}
        for i in arr:
            if i in c:
                c[i] += 1
            else:
                c[i] = 1
        return len(c.values()) == len(set(c.values()))

arr = [-3,0,1,-3,1,1,1,-3,10,0]
Solution = Solution()
ans =  Solution.uniqueOccurrences(arr)
print(ans)