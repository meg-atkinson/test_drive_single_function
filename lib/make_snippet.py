# File: make_snippet.py

# function takes a string as an argument and returns the first five words and then a '...' if there are more than that.
def make_snippet(string):
    words = string.split()
    if len(words) <= 5:
        return string
    else:
        return " ".join(words[:5]) + "..."