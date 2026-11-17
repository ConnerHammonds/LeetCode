class Solution:
    
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        cols = set()
        rows = set() 

        #iterate through row by row and mark columns with zero
        for row in range(len(matrix)):
          for col in range(len(matrix[row])):
            if matrix[row][col] == 0:
              cols.add(col)
              rows.add(row)
        
        #iterate through column by column and mark columns with zero
        for row in range(len(matrix)):
          if row in rows:
            for val in range(len(matrix[row])):
              matrix[row][val] = 0
        
        for col in range(len(matrix[0])):
          if col in cols:
            for val in range(len(matrix)):
              matrix[val][col] = 0
