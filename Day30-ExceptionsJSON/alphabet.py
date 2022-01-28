# exercise from nato alphabet project

import pandas

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# create dictionary from csv of letters/codes
file_df = pandas.read_csv("nato_phonetic_alphabet.csv")
alpha_dict = {row.letter:row.code for (index,row) in file_df.iterrows()}

# create list of phonetics from a user input word
#def generate_phonetic():
#    word = input("Enter a word to translate into phonetics: ")
#    try:
#        letter_list = [alpha_dict[letter.upper()] for letter in word]
#    except KeyError:
#        print("Please enter letters only.")
#        generate_phonetic()
#    else:
#        print(letter_list)

#generate_phonetic()

word = input("Enter a word to translate into phonetics: ")
try:
    letter_list = [alpha_dict[letter.upper()] for letter in word]
except KeyError:
    print("Please enter letters only.")
else:
    print(letter_list)