from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        digit_mapping = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        def backtrack(index, path):
            if index == len(digits):
                result.append("".join(path))
                return

            current_digit = digits[index]
            for char in digit_mapping[current_digit]:
                path.append(char)
                backtrack(index + 1, path)
                path.pop()

        result = []
        backtrack(0, [])
        return result

solution = Solution()
input_digits = "23"

print(solution.letterCombinations(input_digits))