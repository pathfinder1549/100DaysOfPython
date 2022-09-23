import smtplib

my_email = "testEmail@gmail.com"
my_password = "testPW"
with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email,password=my_password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs="recieverAddress@gmail.com",
        msg="Subject:Hello\n\nHello World"
    )