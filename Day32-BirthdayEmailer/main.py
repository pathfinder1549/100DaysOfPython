import os
import pandas
import random
import datetime



### FILE DATA ###
BASE_FOLDER = os.path.dirname(__file__)
BDAYS_PATH = os.path.join(BASE_FOLDER, "birthdays.csv")
LETTER_PATHS = [
    os.path.join(BASE_FOLDER, "letter_templates/letter_1.txt"),
    os.path.join(BASE_FOLDER, "letter_templates/letter_2.txt"),
    os.path.join(BASE_FOLDER, "letter_templates/letter_3.txt")
]

### IMPORT BDAYS ###
try:
    bday_file_df = read_csv(BDAYS_PATH)





##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.




