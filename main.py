"""This is a python program to test anagrams in 5+ letter words in the English Language"""

from english_words import get_english_words_set

web2lowerset = get_english_words_set(['web2'], lower=True)

print(web2lowerset)