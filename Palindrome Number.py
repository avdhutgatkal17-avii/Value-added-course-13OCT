# Palindrome Number :

def isPalindrome(n):
    # Write your code here
    original = n
    reverse = 0

    while n > 0:
        digit = n % 10
        reverse = reverse * 10 + digit
        n//= 10

    return original == reverse