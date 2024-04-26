# You are given an integer array nums consisting of n elements, and an integer k.
# Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. 
# Any answer with a calculation error less than 10-5 will be accepted.

def fx(nums, k):
    if k > len(nums):
        return 0
    c_sum = sum(nums[:k])
    max_avg = c_sum / k
    point = 1
    l = k
    '''
    {{{TIME LIMITE ERROR}}}
    for i in range(k, len(nums)):
        l += 1
        c_sum = sum(nums[point:l])
        point += 1
        max_avg = max(max_avg, c_sum / k)
    return max_avg
    '''
    for i in range(k, len(nums)):
        c_sum += nums[i] - nums[i - k]
        max_avg = max(max_avg, c_sum / k)
    return max_avg

nums = [1,12,-5,-6,50,3]
k = 4
result = fx(nums, k)
print("Result=",result)