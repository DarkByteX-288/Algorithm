#Singly linked list
node0 = [5, None]
node1 = [10, None]
node2 = [20, None]
node3 = [30, None]

node0[1] = node1
node1[1] = node2
node2[1] = node3

head = node0
current = head 
while current is not None:
    print(current[0], end=" -> ")
    current = current[1]

print(None)

#Doble linked list
node1 = [None, 10, None]
node2 = [node1, 20, None]
node3 = [node2, 30, None]

node1[2] = node2
node2[2] = node3

head = node1

print("forward traversal:")
current = head
while current is not None:
    print(current[1],end="<->")
    last = current
    current = current[2]
    print("None")

print("/nBackward traversal:")
current = last 
while current is not None:
    print(current[1],end="<->")
    current = current[0]
print("None")