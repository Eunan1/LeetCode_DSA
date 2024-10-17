# Check if letters in a string have equal numbers of occurences

# Store in a hashmap, then check if all keys are equal

from collections import defaultdict

example_input = "ababab"

def checkOccurences(s):

    dic = defaultdict(int)

    for i in s:
        dic[i] += 1

    frequencies = dic.values()
    
    if len(set(frequencies)) == 1:
        return True
    else: 
        return False

answer = checkOccurences(example_input)
print(answer)
