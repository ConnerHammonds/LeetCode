class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        
        top = 0
        bottom = len(matrix) # 3
        right = len(matrix[0]) # 3
        left = 0

        tot = bottom * right
        res = []

        while True:

          for i in range(left, right): #goes right from top row (+)
            res.append(matrix[top][i])
            if len(res) == tot:
              return res

          top += 1
        
          for i in range(top, bottom): #goes down from right column (+)
            res.append(matrix[i][right-1])
            if len(res) == tot:
              return res
        
          right -= 1

          for i in reversed(range(left, right)): #goes left from bottom row (-)
            res.append(matrix[bottom-1][i])
            if len(res) == tot:
              return res
        
          bottom -= 1

          for i in reversed(range(top, bottom)): #goes up from left column (-)
            res.append(matrix[i][left])
            if len(res) == tot:
              return res

          left += 1

        return res
