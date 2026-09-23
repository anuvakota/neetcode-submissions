class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = collections.defaultdict(set) #hash map creates
        rows = collections.defaultdict(set) 
        squares = collections.defaultdict(set) #key = (r/3,col/3)   

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".": #skip and continue if the box is empty
                    continue
                if ((board[r][c] in rows[r]) or board[r][c] in cols[c] or board[r][c] in squares[(r//3, c//3)]) : #have we already seen the value in the current row or current column that we already in 
                #or is the duplicate in the current square that we area already in
                    return False #detected duplicated
                cols[c].add(board[r][c]) #otherwise add it to the hashmap if not already seen
                rows[r].add(board[r][c])
                squares[r //3, c//3].add(board[r][c])
            
        return True
