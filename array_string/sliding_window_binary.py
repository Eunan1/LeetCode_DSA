s = [1,1,0,1,0,0,1,1,1,1]

# Find the longest substring of 1s after conversion of a 0
# Another way to look at this is longest substring that contains one 0

# Pseudocode

# Sliding window
def find_length(s):
    left = 0
    curr = 0
    ans = 0

    for right in range(len(s)):
        if s[right] == 0:
            curr += 1
        
        while curr > 1:
            if s[left] == 0:
                curr -= 1
            left += 1
    
        ans = max(ans, right - left + 1)

    return ans



answer = find_length(s)
print(answer)

