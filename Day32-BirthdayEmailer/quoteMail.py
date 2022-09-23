import smtplib
import datetime as dt
import os
import random

# file config
base_folder = os.path.dirname(__file__)
data_path = os.path.join(base_folder, "quotes.txt")

def email_string(to, subject, body):
    my_email = "testEmail@gmail.com"
    my_password = "testPW"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email,password=my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=to,
            msg=f"Subject:{subject}\n\n{body}"
        )

def get_quote():
    try:
        with open(data_path, mode="r") as quote_file:
            all_quotes = quote_file.readlines()
            quote = random.choice(all_quotes)
    except FileNotFoundError:
        print("File not found!")
    return quote

def is_friday():
    current_day = dt.datetime.now().weekday()
    if current_day == 4:    # Monday is 0
        return True
    else:
        return False

if is_friday():
    print(get_quote())
    #email_string(get_quote())