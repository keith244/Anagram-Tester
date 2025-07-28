"""This is a python program to test anagrams in 5+ letter words in the English Language"""



from english_words import get_english_words_set
from itertools import combinations,permutations
from wordfreq import word_frequency 
from illegal_words import blacklist
import time



WORD_LENGTH = 5
MAX_WORD_LENGTH = 10
def take_user_input():
    web2lowerset = get_english_words_set(['web2'], lower=True)

    while True:
        user_word= str(input('Enter word you want to test: ')).lower()
        if user_word in ('quit','q','n'):
            return None
        cleaned_user_input= ''.join(c for c in user_word if c.isalpha())    
        if len(cleaned_user_input) < WORD_LENGTH:
            print(f'The word {user_word} is too short. Use a word with a minimum of {WORD_LENGTH} letters!')
        elif len(cleaned_user_input) >MAX_WORD_LENGTH:
            print(f'This word is taking too long to process. Max word length should be {MAX_WORD_LENGTH}')
        else:
            if cleaned_user_input in web2lowerset:
                print('Found it')
                return cleaned_user_input
            else:
                print('No match')
            # return cleaned_user_input

def find_sub_anagrams(word,word_set):
    print(f'You entered {word}')
    print('Trying all combinations')

    # the word is split to individual letters and then recombined in different orders to form a new word
    generated_words = set()

    for i in range (2,len(word)+1):
        perms = permutations(word,i)
        for p in perms:
            candidate = ''.join(p)
            generated_words.add(candidate)
    print(f' Found {len(generated_words)} unique combinations.')

    valid_words= []
    for candidate in sorted(generated_words):
        if candidate in word_set and word_frequency(candidate,'en')>1e-6 and candidate not in blacklist:
            print(f'It exists {candidate}')
            valid_words.append(candidate)
    
    print(f'\nSummary: Found {len(valid_words)} valid words: {valid_words}')
    

web2lowerset = get_english_words_set(['web2'], lower=True)
user_word = take_user_input()
if user_word:
    find_sub_anagrams(user_word, web2lowerset)
else:
    print('Goodbye')
