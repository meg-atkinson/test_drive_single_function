#import function
from lib.count_words import count_words

#returns zero if empty string
def test_returns_zero_if_empty_string():
    assert count_words("") == 0, 'returns zero if empty string'

#returns zero if no string entered
def test_returns_zero_if_no_argument_given():
    assert count_words() == 0, 'returns zero if no argument'

#returns 5 if string of 5
def test_returns_five_if_five_words_long():
    assert count_words("one two three four five") == 5, 'returns 5 if five words long'

#if delimited by punctuation and not space return 1
def test_delimited_by_commas_returns_one():
    assert count_words("one,two,three,four,five,six") == 1, 'returns 1 if delimit with commas'