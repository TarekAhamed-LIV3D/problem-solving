class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False

        for factor in [2, 3, 5]:
            while n % factor == 0:
                n //= factor

        return n == 1

number = 6
solution = Solution()
result = solution.isUgly(number)

print(f"{number} is an ugly number: {result}")
