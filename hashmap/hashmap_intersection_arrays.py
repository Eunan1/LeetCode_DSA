# Compare multiple subarrays within an array to see which numbers ar
# common to all arrays

# Clarifying questions -> Are entries in 1 array guarenteed to be unique?
# If so this opens up opportunity to check for keys > 1
# If not we will need to cross check all hashmaps somehow

# Idea
# Loop through each array ans store in hashmap.
# If

from collections import defaultdict

example_input = [[3, 1, 2, 4, 5], [1, 2, 3, 4], [3, 4, 5, 6]]

def check_arrays(nums):

    dict = defaultdict(int)
    ans = []
    
    for sublist in nums:
        for x in sublist:
            dict[x] += 1

    n = len(nums)
    
    for i in dict:
        if dict[i] == n:
            ans.append(i)
    
    return sorted(ans)

    


answer = check_arrays(example_input)
print(answer)