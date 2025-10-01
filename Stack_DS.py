stack = []

stack.append(10)
stack.append(20)
stack.append(30)

print("Stack after pushes:", stack)

print("Popped:", stack.pop())
print("stack after pop:" ,stack)

print("Top element:", stack[-1])


if not stack:
    print("stack is empty")
else:
    print("Stack is not empty")