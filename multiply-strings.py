class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        result = [0] * (len(num1) + len(num2))

        for i in range(len(num1) - 1, -1, -1):
            carry = 0
            for j in range(len(num2) - 1, -1, -1):
                temp_sum = int(num1[i]) * int(num2[j]) + result[i + j + 1] + carry
                result[i + j + 1] = temp_sum % 10
                carry = temp_sum // 10

            result[i] += carry

        result_str = "".join(map(str, result)).lstrip("0")
        return result_str if result_str else "0"

solution = Solution()
num1 = "2"
num2 = "3"

print(solution.multiply(num1, num2))