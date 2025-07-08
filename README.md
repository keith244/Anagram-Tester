# Anagram Tester

## Description
This CLI app tests *my personal* theory:  
**"All English words with 5+ letters can be rearranged to form other valid English words with equal or fewer letters."**

## Example:
The word great contains the letters g,r,e,a,t which can be rearranged to form the words:
- eat, ate, tea, gate, get, tear, tare, rate, ear, gear e.t.c

as you can see, we can form other words from just the original word without introducing new letters or using the letters more than the number they appear.

## How does it work??
- takes in a user input.
- It then cleans the word inputed by the user to remove special characters, numbers etc.
- Once done, it checks if the word length is greater than or equal to 5 characters if so proceed.
- It then checks if the word exists in the english_words dictionary set.
- If so, proceed. This step helps to ensure only valid english words of 5+ letters are accepted.
- The next step invloves breaking the word to individual letters then forming new combinations from it. 
- Once done, it compares if in any of the combinations the words exists in the english_words dictionary. If so, it is printed out.

Thats it.

## App installation
To install the app, do the following on your machine
1. Clone the repo:
   ```bash
   git clone https://github.com/keith244/Anagram-Tester
   cd project-name (i.e. anagram tester)
2. Create and activate virtual environment:
   ```bash
   - python -m venv venv # or whatever you want to name your virtual env
   - source venv/bin/activate # On windows: venv\scripts\activate

4. Install dependencies
   run the following:
   ```bash
   - pip install -r requirements.txt

## How to run the app
1. Run the following:
   ```bash
   - python main.py
2. Or just hit **Run** on your IDE (i.e. VS Code)


## NOTES
Uses english_words and nltk word sets
Ensure you have internet for nltk.download() on first run.

# Future Improvements
 - Add batch processing for multiple words
 - Export results to CSV/JSON/TXT file
 - Implement different dictionary sources
 - Performance optimization for very long words

# LICENCE
MIT

# AUTHOR
Keith - [Github Profile](https://github.com/keith244)


This project started as a personal curiosity about English language patterns and evolved into a systematic way to test linguistic theories programmatically.
