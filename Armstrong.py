# Check if the Number is Armstrong

def isArmstrong(n):
    # Write your code here
    original = n
    digits = len(str(n))
    total = 0

    while n > 0:
        digit = n % 10 
        total += digit ** digits
        n //= 10

    return total == original