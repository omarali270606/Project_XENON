"""Finger exercise: Implement a 
function that meets the specification"""

def get_min(d): 
    """d a dict mapping letters to ints 
    returns the value in d with the key 
    that occurs first in the alphabet. 
    E.g., if d = {x = 11, b = 12}, 
    get_min returns 12."""
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    lowest = 27
    for key in d.keys():
        if alphabet.index(key) < lowest:
            lowest = alphabet.index(key)
            lowest_key = key
    return d[lowest_key]
