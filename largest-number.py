# Return the Largest Digit in a Number :

def returnLargestDigit(n):
    # Write your code here
    largest = 0

    while n>0:
      digit = n % 10

      if digit > largest:
        largest = digit

      n //= 10

    return largest