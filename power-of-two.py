class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        return n & (n - 1) == 0

number = 16
solution = Solution()
result = solution.isPowerOfTwo(number)

print(f"{number} is a power of two: {result}")
