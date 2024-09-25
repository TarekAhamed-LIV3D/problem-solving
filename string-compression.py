from typing import List

class Solution:
    def compress(self, chars: List[str]) -> int:
        n = len(chars)
        w = 0 
        r = 0   
    
        while r < n:
            char = chars[r]
            count = 0
        
            while r < n and chars[r] == char:
                r += 1
                count += 1
        
            chars[w] = char
            w += 1
        
            if count > 1:
                for x in str(count):
                    chars[w] = x
                    w += 1
    
        return w

chars = ["a","a","a","a","a","b","b","b","c","c","c"]
solution = Solution()
ans = solution.compress(chars)
print(ans)