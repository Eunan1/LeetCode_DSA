# Find subarray withe exactly k odd numbers.
# Another prefix sum question but this time add only odd numbers to curr

from collections import defaultdict

example_input = [1, 1, 2, 1, 1]
k = 3

def findSubarray(nums, k):

    dict_count = defaultdict(int)
    dict_count[0] = 1
    curr = 0
    ans = 0

    for num in nums:
        curr += num % 2
        ans += dict_count[curr - k]
        dict_count[curr] += 1

    return ans

answer = findSubarray(example_input, k)
print(answer)
         
