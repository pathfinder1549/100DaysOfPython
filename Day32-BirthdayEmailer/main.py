from ast import And
import os
import pandas
import random
import datetime
import smtplib

### CONST DATA ###
MY_EMAIL = "testEmail@gmail.com"
MY_PW = "testPW"
BASE_FOLDER = os.path.dirname(__file__)
BDAYS_PATH = os.path.join(BASE_FOLDER, "birthdays.csv")
LETTER_PATHS = [
    os.path.join(BASE_FOLDER, "letter_templates/letter_1.txt"),
    os.path.join(BASE_FOLDER, "letter_templates/letter_2.txt"),
    os.path.join(BASE_FOLDER, "letter_templates/letter_3.txt")
]

### IMPORT BDAYS ###
try:
    bday_file_df = pandas.read_csv(BDAYS_PATH)
    #bday_list = bday_file_df.to_dict(orient="records")
    bday_dict = {(data_row.month, data_row.day): data_row for (index, data_row) in bday_file_df.iterrows()}
    # new_dict = {new_key:new_value for (index, row) in df.iterrows()}
except FileNotFoundError:
    print("File not found.")

### CHECK DATE ###
today = datetime.datetime.now()
today_tuple = (today.month, today.day)

#bdays_matching_month = bday_file_df[bday_file_df["month"] == today.month]
#bdays_matching_day = bdays_matching_month[bdays_matching_month["day"] == today.day]

if today_tuple in bday_dict:
    bday_person = bday_dict[today_tuple]
    letter_path = random.choice(LETTER_PATHS)
    with open(letter_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", bday_person["name"])

# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=MY_EMAIL,password=MY_PW)
#     connection.sendmail(
#         from_addr=MY_EMAIL,
#         to_addrs=bday_person["email"],
#         msg=f"Subject:Happy Bday!\n\n{contents}"
#         )

print(contents)
