
def factorial(n):
"""factorial finder function 
    we use this to implement recursion logic """

    if n == 0:
        return 1
    else:
        return n*factorial(n-1)

#test
print(factorial(3))
