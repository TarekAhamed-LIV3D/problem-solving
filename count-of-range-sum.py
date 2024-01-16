import itertools
class Solution:
    def countRangeSum(self, nums: list[int], lower: int, upper: int) -> int:
        def merge_sort(lo, hi):
            mid = (lo + hi) // 2
            if mid == lo:
                return 0
            count = merge_sort(lo, mid) + merge_sort(mid, hi)
            i = j = mid
            for left in prefix_sum[lo:mid]:
                while i < hi and prefix_sum[i] - left < lower:
                    i += 1
                while j < hi and prefix_sum[j] - left <= upper:
                    j += 1
                count += j - i
            prefix_sum[lo:hi] = sorted(prefix_sum[lo:hi])
            return count
        
        prefix_sum = [0] + list(itertools.accumulate(nums))
        return merge_sort(0, len(prefix_sum))

nums = [-2, 5, -1]
lower = -2
upper = 2
solution = Solution()
result = solution.countRangeSum(nums, lower, upper)

print(f"The number of range sums within the range [{lower}, {upper}] is: {result}")