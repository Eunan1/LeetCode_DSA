# Compare to strings to see if they're equal after a backspace of an
# element represented by e

example1 = "ab#c"
example2 = "ad#c"

def backspace(s, t):
    def helper(string):

        stack = []

        for c in string:
            if c != "#":
                stack.append(c)
            
            elif stack:
                stack.pop()

        print("".join(stack))
        return "".join(stack)
        
    
    return helper(s) == helper(t)


ans = backspace(example1, example2)
print(ans)