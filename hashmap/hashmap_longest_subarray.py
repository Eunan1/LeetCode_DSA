# Find longest subarray with at most 2 unique elements


# Sliding window question using a hashmap to keep a log of
# the value that appears and it's frequency

# If more than k values appear the sliding window deletes,
# until there is less than k elements again.

# The key keeps track of the frequency.

from collections import defaultdict

input = 'eceba'
k = 2

def find_longest_substring(s, k):

    dict = defaultdict(int)
    left = 0
    ans = 0

    for right in range(len(s)):
        dict[s[right]] += 1

        while len(dict) > k:
            dict[s[left]] -= 1
            if dict[s[left]] == 0:
                del dict[s[left]]
            
            left += 1

        ans = max(ans, right - left + 1)
    
    return ans

answer = find_longest_substring(input, k)
print(answer)

    



