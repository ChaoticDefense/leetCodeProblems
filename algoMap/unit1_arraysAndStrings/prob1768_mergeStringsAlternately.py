# You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

# Return the merged string.

 

# Example 1:

# Input: word1 = "abc", word2 = "pqr"
# Output: "apbqcr"
# Explanation: The merged string will be merged as so:
# word1:  a   b   c
# word2:    p   q   r
# merged: a p b q c r

# Example 2:

# Input: word1 = "ab", word2 = "pqrs"
# Output: "apbqrs"
# Explanation: Notice that as word2 is longer, "rs" is appended to the end.
# word1:  a   b 
# word2:    p   q   r   s
# merged: a p b q   r   s

# Example 3:

# Input: word1 = "abcd", word2 = "pq"
# Output: "apbqcd"
# Explanation: Notice that as word1 is longer, "cd" is appended to the end.
# word1:  a   b   c   d
# word2:    p   q 
# merged: a p b q c   d



class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # Length of words
        A = len(word1)
        B = len(word2)
        
        # Init output
        s = []
        
        # Init pointers, one for each word
        i, j = 0, 0
        
        # Word number tracker, start with word1, then alternate between words
        word = 1
        
        while i < A and j < B:
            if word == 1:
                s.append(word1[i])
                i += 1
                word = 2
            else:
                s.append(word2[j])
                j += 1
                word = 1
        
        if i < A:
            s.append(word1[i::])
        else:
            s.append(word2[j::])
        
        return ''.join(s)
    

word1 = "abc"
word2 = "pqr"
print(Solution().mergeAlternately(word1,word2))