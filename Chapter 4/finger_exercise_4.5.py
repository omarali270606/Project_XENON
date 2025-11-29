"""
Finger exercise: Use find to implement a 
function satisfying the specification
"""

def find_last(s, sub): 
    """s and sub are non-empty strings 
Returns the index of the last occurrence of sub in s. 
Returns None if sub does not occur in s"""
    if sub in s:
        inversed_s = s[::-1]
        inversed_sub = sub[::-1]
        indexes = len(s)
        inversed_index = inversed_s.find(inversed_sub)
        index = indexes - inversed_index - len(sub)
        return index
    else:
        return None