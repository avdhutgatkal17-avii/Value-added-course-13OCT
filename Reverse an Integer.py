# Reverse an Integer :

def reverseInteger(n):
    # Write your code here
  reverse = 0

  while n > 0:
    digit = n % 10
    reverse = reverse * 10 + digit
    n //= 10

  return reverse