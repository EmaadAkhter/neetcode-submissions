class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
         for i in range(9):
            seen_r=set()
            seen_c=set()
            for j in range(9):
                if board[i][j] in seen_r and board[i][j] != '.' :
                    return False
                elif board[j][i] in seen_c and board[j][i] != '.':
                    return False
                
                else:
                    seen_r.add(board[i][j])
                    seen_c.add(board[j][i])

         for box_row in range(3):
            for box_col in range(3):
                seen_box = set()
                for i in range(3):
                    for j in range(3):
                        row = box_row * 3 + i
                        col = box_col * 3 + j
                        cell = board[row][col]
                        
                        if cell != '.' and cell in seen_box:
                            return False
                        if cell != '.':
                            seen_box.add(cell)
            
         return True    