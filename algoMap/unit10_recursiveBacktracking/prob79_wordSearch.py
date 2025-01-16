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
        foundWord = [False]
        w_len = len(word)
        
        m = len(board)
        n = len(board[0])
        
        traveledSpaces = []
        
        def backtrack(i,j,p):
            if board[i][j] != word[p]:
                return
            
            p += 1
            if p == w_len:
                foundWord[0] = True
                return
            
            traveledSpaces.append([i, j])
            
            # Choosing direction to move
            # RIGHT
            if j < n-1 and [i, j+1] not in traveledSpaces:
                backtrack(i, j+1, p)
            
            # DOWN    
            if i < m-1 and [i+1, j] not in traveledSpaces:
                backtrack(i+1, j, p)
                
            # LEFT
            if j > 0 and [i, j-1] not in traveledSpaces:
                backtrack(i, j-1, p)
            
            # UP
            if i > 0 and [i-1, j] not in traveledSpaces:
                backtrack(i-1, j, p)
            
            traveledSpaces.pop()              
        
        for i in range(m):
            for j in range(n):
                backtrack(i,j,0)
                 
        return foundWord[0]
    
board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "GUY"
print(Solution().exist(board, word))