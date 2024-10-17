nums = [10, 5, 2, 6]
k = 100


def numSubarrayProductLessThanK(nums, k):
    if k < 1:
        return 0
    
    left = 0
    curr = 1
    ans = 0

    for right in range(len(nums)):
        curr *= nums[right]
        
        if curr >= k:
            curr //= nums[left]
            left += 1

        ans = max(ans, right - left + 1)
    
    return ans

answer = numSubarrayProductLessThanK(nums, k)
print(answer)