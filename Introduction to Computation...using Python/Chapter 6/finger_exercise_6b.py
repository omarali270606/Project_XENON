# shows if a word is a palindrome (can be reversed) like heh or ekke etc

def is_palindrome(text: str):
    if len(text) < 2:
        return True
    else:
        return text[0]==text[-1] and is_palindrome(text[1:-1])