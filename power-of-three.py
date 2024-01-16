class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False

        max_power_of_three = 3**19
        return max_power_of_three % n == 0

number = 27
solution = Solution()
result = solution.isPowerOfThree(number)

print(f"{number} is a power of three: {result}")