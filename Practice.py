#double linked list 
node0 = [None, 10, None]
node1 = [node0, 20, None]
node2 = [node1, 30, None]
node3 = [node2, 40, None]

node0[1] = node1
node1[1] = node2
node2[1] = node3
head = node0

print("forward traversal")
current = head
while current is not None:
    print(current[1], end="<->")
    last = current 
    current = current[2]
    print["None"] 

print("/nBackward traversal:")
current = last 
while current is not None:
    print(current[1], end="<->")
    current = current[0]
print("None")