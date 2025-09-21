def push(stack, item):
    stack.append(item)

def pop(stack):
    if not stack:
        return "underflow! Stack is empty"
    return stack.pop()

def peek (stack):
    if not stack:
        return ("stack is not empty")
    return stack[-1]

def is_empty(stack):
    return len(stack) == 0

stack = []

push(stack, 10)
push(stack, 20)
push(stack, 30)
print(stack)

a=peek(stack)
print('after peek ', a)

pop(stack)
pop(stack)
pop(stack)

print(is_empty(stack))


