sample_input = "({[]})"

def matchBracket(s):

    match = {"{": "}", "[": "]", "(": ")"}
    stack = []

    for c in s:
        if c in match:
            stack.append(c)
        else:
            if not stack:
                return False
            
            previous_opening = stack.pop()
            if match[previous_opening] != c: 
                return False
            
    return not stack

answer = matchBracket(sample_input)
print(answer)
