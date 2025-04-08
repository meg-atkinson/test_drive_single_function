#Import function
from lib.make_snippet import make_snippet

#test - returns empty string if no words
def test_empty_string_if_empty_string():
    assert make_snippet("") == "", 'returns empty string if given empty string'
#test - returns first five words if five words long
def test_returns_string_if_five_long():
    assert make_snippet("one two three four five") == "one two three four five", 'returns string if five words long'
#test - returns all words if fewer than five words 
def test_returns_string_if_shorter_than_five():
    assert make_snippet("one two three") == "one two three", 'returns string if fewer than five words long'
#test - returns first five words plus "..." if over five words
def test_if_over_five_long():
    assert make_snippet("one two three four five six seven") == "one two three four five...", 'returns truncated string if over five words long'
# test with punctuation
def test_if_include_punctuation():
    assert make_snippet("one, two, three, four and five") == "one, two, three, four and...", 'returns truncated string if over five words long'
# test for delimited by commas returns just as one word - ie only spaces count
def test_delimited_by_commas_returns_string():
    assert make_snippet("one,two,three,four,five,six") == "one,two,three,four,five,six", 'returns truncated string if over five words long'