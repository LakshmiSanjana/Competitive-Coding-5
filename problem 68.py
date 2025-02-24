#  https://leetcode.com/problems/valid-sudoku/

# Time Complexity : O(1) = 9 x 9 = 81 interations
# Space Complexity : O(1) 
# Did this code successfully run on Leetcode : YES
# Any problem you faced while coding this : NO


# Your code here along with comments explaining your approach


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        box = defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                
                if board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in box[(r//3,c//3)]:
                    return False
                
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                box[(r//3,c//3)].add(board[r][c])
        
        return True

        