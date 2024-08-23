from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Get dimensions of matrix
        m = len(matrix)
        n = len(matrix[0])
        
        # Total number of elements in matrix, used essentially "flatten" matrix
        T = m * n
        
        # Set up L and R pointers based on "flattened" matrix
        L = 0
        R = T - 1
        
        # Binary search
        while L <= R:
            M = L + ((R-L) // 2)
            
            # Get locations within matrix based on M
            i = M // n
            j = M % n
            
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] < target:
                L = M + 1
            else:
                R = M - 1
        
        return False
    
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 61
print(Solution().searchMatrix(matrix, target))