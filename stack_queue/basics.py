
stack = []

stack.append(1)
stack.append(2)
stack.append(3)

print(stack[-1])

stack.pop()

print(stack[-1])

stack.pop()

print(len(stack))

print(not stack) # Returns false if it is not empty