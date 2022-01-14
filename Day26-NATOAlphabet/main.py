import pandas

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# create dictionary from csv of letters/codes
file_df = pandas.read_csv("nato_phonetic_alphabet.csv")
alpha_dict = {row.letter:row.code for (index,row) in file_df.iterrows()}

# create list of phonetics from a user input word
word = input("Enter a word to translate into phonetics: ")
letter_list = [alpha_dict[letter.upper()] for letter in word]
print(letter_list)