# You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.

# Evaluate the expression. Return an integer that represents the value of the expression.

# Note that:

#     The valid operators are '+', '-', '*', and '/'.
#     Each operand may be an integer or another expression.
#     The division between two integers always truncates toward zero.
#     There will not be any division by zero.
#     The input represents a valid arithmetic expression in a reverse polish notation.
#     The answer and all the intermediate calculations can be represented in a 32-bit integer.

 

# Example 1:

# Input: tokens = ["2","1","+","3","*"]
# Output: 9
# Explanation: ((2 + 1) * 3) = 9

# Example 2:

# Input: tokens = ["4","13","5","/","+"]
# Output: 6
# Explanation: (4 + (13 / 5)) = 6

# Example 3:

# Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
# Output: 22
# Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5

class Solution:
    def evalRPN(self, tokens: list[str]) -> int:

        stk = []
        
        for token in tokens:
            if token == "+":
                # Addition
                summ = stk[-1] + stk[-2]
                stk.pop()
                stk.pop()
                stk.append(summ)
            elif token == "-":
                # Subtraction
                diff = stk[-2] - stk[-1]
                stk.pop()
                stk.pop()
                stk.append(diff)
            elif token == "*":
                # Multiplication
                prod = stk[-1] * stk[-2]
                stk.pop()
                stk.pop()
                stk.append(prod)  
            elif token == "/":
                # Division (rounds towards zero)
                quot = int(stk[-2] / stk[-1])
                stk.pop()
                stk.pop()
                stk.append(quot)
            else:
                stk.append(int(token))
        
        return stk[0]
    
# tokens = ["2","1","+","3","*"]
# tokens = ["4","13","5","/","-"]
tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
print(Solution().evalRPN(tokens))