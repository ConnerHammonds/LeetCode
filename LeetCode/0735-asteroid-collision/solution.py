class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
      stk = []

      for num in asteroids:
        if num >= 0: #append positive number
          stk.append(num)
      
        else: #if negative
        
          while True:

            if len(stk) == 0 or stk[-1] <= 0: #check if stack is empty or top is negative
              stk.append(num)
              break

            elif stk[-1] == abs(num): #equal magnitute, pop the stack and don't append
              stk.pop()
              break

            elif stk[-1] < abs(num): #if negative number is greater magnitude, delete positive
              stk.pop()
            else:
              break
          
      return stk
