# Written by Jake Foiles, Mar. 2023
# Determines if parentheses ((), {}, or []) are closed correctly in a string
# The string will consist only of brackets, in this version

s = r"(){}[]"
#s = r"({[]})"
#s = r"}()"

# Initial solution - good enough, but not very extensible (violates DRY)
# def valid_parentheses(s):
#     char_stack = []

#     for ch in s:
#         if len(char_stack) != 0 and ch == ')':
#             if char_stack.pop() != '(':
#                 return False
#         elif len(char_stack) != 0 and ch == '}':
#             if char_stack.pop() != '{':
#                 return False
#         elif len(char_stack) != 0 and ch == ']':
#             if char_stack.pop() != '[':
#                 return False
#         else:
#             char_stack.append(ch)
    
#     return len(char_stack) == 0

# Alternative solution heavily based upon NeetCode's
def valid_parentheses(s):
    char_stack = []
    bracket_mapping = { ")" : "(", "}" : "{", "]" : "[" }

    for ch in s:
        if ch in bracket_mapping:
            if len(char_stack) == 0:
                return False
            elif char_stack.pop() != bracket_mapping[ch]:
                return False
        else:
            char_stack.append(ch)
    
    return len(char_stack) == 0

print(valid_parentheses(s))