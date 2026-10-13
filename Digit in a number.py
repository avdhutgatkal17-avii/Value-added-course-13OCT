# Digit in a number

class Solution:
    def digitCounts(self, n: int) -> int:
        # Write your solution here
      if n == 0:
        return 1

      count = 0
      while n>0:
        count +=1
        n//=10

      return count