from typing import List

class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        x = len(nums1)
        y = len(nums2)
        arr1, arr2 = [], []
        for i in range(x):
            if  nums1[i] not in nums2:
                if  nums1[i] not in arr1:
                    arr1.append(nums1[i])
        for i in range(y):
            if  nums2[i] not in nums1:
                if  nums2[i] not in arr2:
                    arr2.append(nums2[i])
        arr = [arr1, arr2]
        return arr
        
nums1 = [1,2,3,4,5]
nums2 = [6,7,8,9]
Solution = Solution()
ans = Solution.findDifference(nums1, nums2)
print(ans)