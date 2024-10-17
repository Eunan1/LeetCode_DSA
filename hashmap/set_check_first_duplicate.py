s = "abcdefdand"

def check_duplicate(s):

    seen = set()

    for i in s:
        if i in seen:
            return i 
        seen.add(i)

    return False

answer = check_duplicate(s)
print(answer)