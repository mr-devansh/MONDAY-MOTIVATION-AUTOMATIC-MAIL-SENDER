import smtplib
import datetime as dt
import random

MAIL = "-----your mail-----"
PASS = "-----your password-----"
NOW = dt.datetime.now()
WEEKDAY = NOW.weekday()

if WEEKDAY==0:

    with open("quotes.txt") as FILE:
        ALL_QUOTES = FILE.readlines()
        CURRENT_QUOTE = random.choice(ALL_QUOTES)

    with smtplib.SMTP("smtp.gmail.com", port = 587) as connection:
        connection.starttls()
        connection.login(user=MAIL, password=PASS)
        connection.sendmail(from_addr=MAIL, to_addrs="-----receiver's email address-----", msg=f"Subject:MONDAY'S MOTIVATION\n\n{CURRENT_QUOTE}")
        connection.close() 