# Written by Jake Foiles, Mar. 2023
# A solution to the most basic anagram detection DSA question

s, t = "anagram", "nagaram"
#s, t = "rat", "car"

def is_anagram(s, t):
    if len(s) != len(t):
        return False

    s_chars, t_chars = {}, {}
    for i in range(len(s)):
        s_char, t_char =  s[i], t[i]
        
        if s[i] not in s_chars:
            s_chars[s_char] = 1
        else:
            s_chars[s_char] = s_chars[s_char] + 1

        if t[i] not in t_chars:
            t_chars[t_char] = 1
        else:
            t_chars[t_char] = t_chars[t_char] + 1

    return s_chars == t_chars

print(is_anagram(s, t))

# Alternative option - loop through s and add each char to a dict
#    Then, loop through t and see if each char is in s_dict (and equal)
