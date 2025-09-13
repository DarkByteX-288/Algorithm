#  Reverse an Array
arr = [1, 2, 3, 4, 5]
left = 0
right = len(arr) - 1
while left < right:
    arr[left], arr[right] = arr[right], arr[left]
    left += 1
    right -= 1
print("Reversed Array:", arr)

#  Find Maximum and Minimum in an Array
arr = [7, 2, 9, 4, 5]
max_val = arr[0]
min_val = arr[0]
for i in range(1, len(arr)):
    if arr[i] > max_val:
        max_val = arr[i]
    if arr[i] < min_val:
        min_val = arr[i]
print("Max:", max_val, "Min:", min_val)

#  Calculate Sum of Array Elements
arr = [1, 2, 3, 4, 5]
total = 0
for i in range(len(arr)):
    total += arr[i]
print("Sum:", total)

#  Find the Second Largest Element
arr = [7, 2, 9, 4, 5]
first = second = float('-inf')
for i in arr:
    if i > first:
        second = first
        first = i
    elif i > second and i != first:
        second = i
print("Second Largest:", second)

#  Count Occurrences of an Element
arr = [1, 2, 3, 2, 2, 4]
element = 2
count = 0
for i in arr:
    if i == element:
        count += 1
print(f"Occurrences of {element}:", count)

#  Remove Duplicates from an Array (without using Set)
arr = [1, 2, 2, 3, 4, 4, 5]
unique = []
for i in arr:
    if i not in unique:
        unique.append(i)
print("Array without duplicates:", unique)

#  Left Rotate an Array by 1
arr = [1, 2, 3, 4, 5]
first = arr[0]
for i in range(1, len(arr)):
    arr[i-1] = arr[i]
arr[-1] = first
print("Left Rotated by 1:", arr)

#  Right Rotate an Array by k Steps
arr = [1, 2, 3, 4, 5]
k = 2
n = len(arr)
for step in range(k):
    last = arr[-1]
    for i in range(n-1, 0, -1):
        arr[i] = arr[i-1]
    arr[0] = last
print(f"Right Rotated by {k}:", arr)

#  Find the Missing Number in an Array of 1..n
arr = [1, 2, 4, 5]
n = 5
expected_sum = n * (n + 1) // 2
actual_sum = 0
for i in arr:
    actual_sum += i
missing = expected_sum - actual_sum
print("Missing Number:", missing)

#  Find Pairs in Array with a Given Sum
arr = [1, 2, 3, 4, 5]
target_sum = 5
print("Pairs with sum", target_sum, ":")
for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        if arr[i] + arr[j] == target_sum:
            print(f"({arr[i]}, {arr[j]})")