class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        x =  set('aeiou')
        y = 0
        z = 0
        a = len(s)
        
        for i in range(a):
            if s[i] in x:
                z += 1  
            if i >= k and s[i-k] in x:
                z -= 1   
            if i >= k-1:
                y = max(y, z) 
        return y
                
        
Solution = Solution()
s =  "aeiou"
k = 2
ans = Solution.maxVowels(s,k)
print(ans)