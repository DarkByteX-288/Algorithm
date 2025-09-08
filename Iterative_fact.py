#this program calculates factorial of a number using iterative approach

def factorial(n):

    if n == 0:
        return 1
    
    fact = 1
    for i in range(1, n+1):
        fact *= i
    return fact


print(factorial(5))  # Output: 120
print(factorial(0))  # Output: 1

