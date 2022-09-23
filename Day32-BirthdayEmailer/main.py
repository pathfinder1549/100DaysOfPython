import smtplib
import datetime as dt

#my_email = "testEmail@gmail.com"
#my_password = "testPW"
#with smtplib.SMTP("smtp.gmail.com") as connection:
#    connection.starttls()
#    connection.login(user=my_email,password=my_password)
#    connection.sendmail(
#        from_addr=my_email,
#        to_addrs="recieverAddress@gmail.com",
#        msg="Subject:Hello\n\nHello World"
#    )

now = dt.datetime.now()
print(now)

date_of_birth = dt.datetime(year=1989, month=10, day=17)