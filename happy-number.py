class Solution:
    def isHappy(self, n: int) -> bool:
        def get_next(number):
            result = 0
            while number > 0:
                digit = number % 10
                result += digit ** 2
                number //= 10
            return result

        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = get_next(n)

        return n == 1

number = 19
solution = Solution()
result = solution.isHappy(number)

print(f"{number} is a happy number: {result}")
