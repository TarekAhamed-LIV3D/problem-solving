from typing import List

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        result = [1] * (rowIndex + 1)

        for i in range(1, rowIndex):
            for j in range(i, 0, -1):
                result[j] += result[j - 1]

        return result

row_index = 3
solution = Solution()
result = solution.getRow(row_index)

print(f"Pascal's Triangle row at index {row_index}: {result}")
