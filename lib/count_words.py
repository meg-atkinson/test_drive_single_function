#File: count_words.py
#function that takes a string as an argument 
# and returns the number of words in that string.
def count_words(string=""):
    words = string.split()
    return len(words)