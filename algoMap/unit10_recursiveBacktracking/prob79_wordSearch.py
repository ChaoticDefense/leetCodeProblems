# Given an m x n grid of characters board and a string word, return true if word exists in the grid.

# The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

 

# Example 1:

# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
# Output: true

# Example 2:

# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
# Output: true

# Example 3:

# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
# Output: false

from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # Grab length of word
        w_len = len(word)
        
        # Get dimensions of board
        m = len(board)
        n = len(board[0])
        
        # Special case: board is only 1x1
        if m == 1 and n == 1:
            return board[0][0] == word
        
        # Recursive function
        def backtrack(i,j,p):
            # If reached end of word, then we found the whole word
            if p == w_len:
                return True
            
            # If we went too far in either direction or the space does match current letter
            if i < 0 or i >= m or j < 0 or j >= n or board[i][j] != word[p]:
                return False
            
            # Set board to empty since we traversed it
            tmp = board[i][j]
            board[i][j] = ''
            
            # Check each direction
            if backtrack(i, j+1, p+1) or backtrack(i+1, j, p+1) or backtrack(i, j-1, p+1) or backtrack(i-1, j, p+1):
                return True

            # Backtracking, return letter at current position and move on to next letter
            board[i][j] = tmp
            return False          
        
        # Loop through board until starting letter is found
        for i in range(m):
            for j in range(n):
                # If the word hasnt been found, keep looking
                if backtrack(i,j,0):
                    return True
                 
        return False
    
board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCCED"
print(Solution().exist(board, word))