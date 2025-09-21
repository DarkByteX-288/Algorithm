

def factorial(n):
"""factorial finder function 
    we use this to implement recursion logic """

    if n == 0:
        return 1
    else:
        return n*factorial(n-1)

#test of function
print(factorial(3))


#This program calculates fibonacci of a number using recursive approach
def febo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1 
    else:
        return febo(n-1) + febo(n-2)

# use for loop to print the first fibonacchi numbers 
for i in range(7):
    print (f"febo({i}) = {febo(i)}")
