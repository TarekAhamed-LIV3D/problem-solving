class Solution:
    def addDigits(self, num: int) -> int:
        while num >= 10:
            digit_sum = 0
            while num > 0:
                digit_sum += num % 10
                num //= 10
            num = digit_sum
        return num

number = 38
solution = Solution()
result = solution.addDigits(number)

print(f"The digital root of {number} is: {result}")
