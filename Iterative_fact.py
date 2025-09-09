def factorial(n):
    '''This function is used to print factorial off a number 
    main resaon of this is to implement iterative logic for factorial '''
    
    if n == 0:
        return 1
    fact = 1
    for i in range(1, n+1):
        fact *= i
    return fact

#test
print(factorial(5))  # Output: 120
print(factorial(0))  # Output: 1

