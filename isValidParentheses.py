from collections import deque

def isValidParentheses(str):
    if(len(str) %2 != 0): return False
    myStack = deque()
    for char in str:
        if char == '(' or char == '{' or char == '[':
            myStack.append(char)
        elif (char  == ')' and myStack and myStack[-1]== '('):
            myStack.pop()
        elif (char  == '}' and myStack and myStack[-1]== '{'):
            myStack.pop()
        elif (char  == ']' and myStack and myStack[-1]== '['):
            myStack.pop()

    if (myStack): return False
    else: return True

print(isValidParentheses("[{()}]"))
print(isValidParentheses("[{()]"))
print(isValidParentheses("[((]"))
