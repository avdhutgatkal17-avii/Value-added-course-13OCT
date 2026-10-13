# Factorial of a Given Number :
def factorial(n):
    # Write your code here
    fact = 1

    for i in range (1,n + 1):
        fact *= i 

    return fact 