"""queue = [10,20,30,40]

stack = []
while queue:
    stack.append(queue.pop(0))

while stack:
    queue.append(stack.pop())

print(queue)
"""

Q = [12,1,3,4,5]

max_value = Q[0]

for i in Q:
    if i > max_value:
        max_value = i  

print(max_value)
