"""This is a python program to test anagrams in 5+ letter words in the English Language"""

import nltk
from nltk.corpus import words
from english_words import get_english_words_set
from itertools import combinations,permutations
import itertools

# print(web2lowerset)
nltk.download('words')
WORD_LENGTH = 5
def take_user_input():
    web2lowerset = get_english_words_set(['web2'], lower=True)
    user_word= str(input('Enter word you want to test: ')).lower()
    while user_word not in ('quit','q','n'):
        cleaned_user_input= ''.join(c for c in user_word if c.isalpha())    
        if len(cleaned_user_input) < WORD_LENGTH:
            print(f'The word {user_word} is too short. Use a word with a minimum of {WORD_LENGTH} letters!')
        else:
            if cleaned_user_input in web2lowerset:
                print('Found it')
            else:
                print('No match')
        break
    return cleaned_user_input

def rearrange_word_and_compare(word_set):
    word = take_user_input()
    print(f'You entered {word}')
    print('Trying all combinations')
    # the word is split to individual letters and then recombined in different orders to form a new word
    all_combinations = set()
    for i in range (2,len(word)+1):
        perms = permutations(word,i)
        for p in perms:
            joined = ''.join(p)
            if joined in word_set:
                all_combinations.add(joined)
    print(sorted(all_combinations))
    

print(take_user_input())
web2lowerset =get_english_words_set(['web2'],lower=True)
rearrange_word_and_compare(web2lowerset)
