class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(list)
        cols = defaultdict(list)
        squares = defaultdict(list)

        for row in range(len(board)):
            for col, c in enumerate(board[row]):
                if c == ".":
                    continue
                if c in rows[row] or c in cols[col] or c in squares[(col // 3, row // 3)]:
                    return False
                
                rows[row].append(c)
                cols[col].append(c)
                squares[(col // 3, row // 3)].append(c)
        
        return True
                
