
# Create and Traverse a Singly Linked List
node1 = [10, None]  # Each node is a list: [data, next]
node2 = [20, None]
node3 = [30, None]
node1[1] = node2
node2[1] = node3
head = node1

# Traverse
current = head
while current is not None:
    print(current[0], end=" -> ")
    current = current[1]
print(None)

#  Insert at End
new_node = [40, None]
current = head
while current[1] is not None:
    current = current[1]
current[1] = new_node

# Traverse after insertion at end
current = head
while current is not None:
    print(current[0], end=" -> ")
    current = current[1]
print(None)

#  Insert at Start
new_head = [5, head]
head = new_head

# Traverse after insertion at start
current = head
while current is not None:
    print(current[0], end=" -> ")
    current = current[1]
print(None)

#  Reverse Singly Linked List
prev = None
current = head
while current is not None:
    next_node = current[1]
    current[1] = prev
    prev = current
    current = next_node
head = prev

# Traverse after reverse
current = head
while current is not None:
    print(current[0], end=" -> ")
    current = current[1]
print(None)

#  Find Middle of Linked List
slow = head
fast = head
while fast is not None and fast[1] is not None:
    slow = slow[1]
    fast = fast[1][1]
print("Middle node value:", slow[0])

#  Detect Loop in Linked List
# Create a loop for demonstration
# Uncomment below to create a loop
# node3[1] = node1  # Creates a loop

slow = head
fast = head
has_loop = False
while fast is not None and fast[1] is not None:
    slow = slow[1]
    fast = fast[1][1]
    if slow == fast:
        has_loop = True
        break
print("Loop detected:" if has_loop else "No loop detected.")

#  Doubly Linked List Reverse 
# Each node: [data, prev, next]
dnode1 = [10, None, None]
dnode2 = [20, dnode1, None]
dnode3 = [30, dnode2, None]
dnode1[2] = dnode2
dnode2[2] = dnode3
dhead = dnode1

# Reverse doubly linked list
current = dhead
prev = None
while current is not None:
    next_node = current[2]
    current[2] = prev
    current[1] = next_node
    prev = current
    current = next_node
dhead = prev

# Traverse reversed doubly linked list
current = dhead
while current is not None:
    print(current[0], end=" <-> ")
    current = current[2]
print(None)