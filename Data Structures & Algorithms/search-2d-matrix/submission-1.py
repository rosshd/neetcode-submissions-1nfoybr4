class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        
        # Treat as 1D array of size m*n
        l, r = 0, m * n - 1  # Inclusive bounds
        
        while l <= r:
            mid = (l + r) // 2
            row = mid // n     # Which row
            col = mid % n      # Which column
            
            val = matrix[row][col]
            
            if val < target:
                l = mid + 1
            elif val > target:
                r = mid - 1
            else:
                return True
                
        return False