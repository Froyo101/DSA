# Written by Jake Foiles, Mar. 2023
# A solution to the most basic palindrome detection DSA question

s = "A man, a plan, a canal: Panama"
#s = "aba"
#s = "ree"

s = s.strip().lower() # Ignore case, trailing whitespace

ASCII_a = ord("a")
ASCII_z = ord("z")
ASCII_0 = ord("0")
ASCII_9 = ord("9")

# Ensures the current character is alphanumeric
def alpha_num(ch):
    return (ASCII_a <= ord(ch) <= ASCII_z) or (ASCII_0 <= ord(ch) <= ASCII_9)

def palindrome(s):
    l, r = 0, len(s) - 1 # Pointers start from opposite ends of the list
    
    while l < r:
        while not alpha_num(s[l]):
            l += 1
        while not alpha_num(s[r]):
            r -= 1
        
        if s[l] != s[r]:
            return False
        
        l, r = l + 1, r - 1
    
    return True

print(palindrome(s))

# Solution employing regex
# import re
# class Solution(object):
#     def isPalindrome(self, s):
#         """
#         :type s: str
#         :rtype: bool
#         """
#         cleanS = s.lower().strip()
#         print(cleanS)
#         cleanS = re.sub('[^a-z0-9]', '', cleanS)
#         print(cleanS)

#         for i in range(int(len(cleanS)/2)):
#             if cleanS[i] != cleanS[-i - 1]:
#                 return False
#         return True