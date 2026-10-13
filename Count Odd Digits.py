# Count Odd Digits :

def countOddDigits(n):
    # Write your code here
    count = 0

    if n == 0:
       return 0

    while n > 0:
        digit = n % 10

        if digit % 2 != 0:
          count +=1

        n//= 10

    return count