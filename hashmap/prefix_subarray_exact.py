# Find number of subarrays with an exact sum of k.

# Add each element to the dictionary and increase its frequency key

# If the element current prefix - expected sum exists, it is added to answer

from collections import defaultdict

example_input = [1, 2, 1, 2, 1]
k = 3

def findSubarrays(nums, k):

    count_dic = defaultdict(int)
    count_dic[0] = 1 # The sum is 0 to begin. So we log the 0 once.
    curr = 0
    ans = 0

    for num in nums:
        curr += num
        ans += count_dic[curr - k]
        count_dic[curr] += 1        # Increment index of current prefix

    return ans


answer = findSubarrays(example_input, k)
print(answer)
