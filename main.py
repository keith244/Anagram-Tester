"""This is a python program to test anagrams in 5+ letter words in the English Language"""

import nltk
# from nltk.corpus import words
from english_words import get_english_words_set
from itertools import combinations,permutations
# import itertools
# import english_words
from wordfreq import word_frequency 

# print(web2lowerset)
nltk.download('words')

WORD_LENGTH = 5
def take_user_input():
    web2lowerset = get_english_words_set(['web2'], lower=True)

    while True:
        user_word= str(input('Enter word you want to test: ')).lower()
        if user_word in ('quit','q','n'):
            return None
        cleaned_user_input= ''.join(c for c in user_word if c.isalpha())    
        if len(cleaned_user_input) < WORD_LENGTH:
            print(f'The word {user_word} is too short. Use a word with a minimum of {WORD_LENGTH} letters!')
        else:
            if cleaned_user_input in web2lowerset:
                print('Found it')
                return cleaned_user_input
            else:
                print('No match')
            # return cleaned_user_input

def find_combination_in_dictionary(word,word_set):
    print(f'You entered {word}')
    print('Trying all combinations')
    # the word is split to individual letters and then recombined in different orders to form a new word
    all_combinations = set()

    for i in range (2,len(word)+1):
        perms = permutations(word,i)
        for p in perms:
            combinations = ''.join(p)
            all_combinations.add(combinations)
    print(f' Found {len(all_combinations)} unique combinations.')

    valid_combinations= []
    for combination in sorted(all_combinations):
        if combination in word_set and word_frequency(combination,'en')>1e-6:
            print(f'It exists {combination}')
            valid_combinations.append(combination)
    
    print(f'\nSummary: Found {len(valid_combinations)} valid words: {valid_combinations}')
    

web2lowerset = get_english_words_set(['web2'], lower=True)
user_word = take_user_input()
if user_word:
    find_combination_in_dictionary(user_word, web2lowerset)
else:
    print('Goodbye')
