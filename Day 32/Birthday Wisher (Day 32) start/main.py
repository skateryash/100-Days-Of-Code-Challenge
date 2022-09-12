import random
import smtplib
import datetime as dt
import random

MY_EMAIL = "mrfrek78@gmail.com"
MY_PASSWORD = "jzwqbvjcwoinxuye"

now = dt.datetime.now()
weekday = now.weekday()

if weekday == 11:
    with open("quotes.txt") as data:
        quotes = [line for line in data.readlines()]
        quote_of_the_day = random.choice(quotes)
        # print(quote_of_the_day)

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="creativehub371@gmail.com",
            msg=f"Subject: Monday Motivation\n\n{quote_of_the_day}"
        )




year = now.year
# month = now.month
# day_of_week = now.weekday()
print(now)
#
# date_of_birth = dt.datetime(year=2001, month=7, day=3, hour=7)
# print(date_of_birth)