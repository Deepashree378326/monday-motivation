import smtplib
import random
import os

# Get secure values from environment
my_email = os.environ.get("EMAIL_ADDRESS")
password = os.environ.get("EMAIL_PASSWORD")
recipients = os.environ.get("RECIPIENTS")

# Convert comma separated emails into list
recipient_list = recipients.split(",")

# Read quotes
with open("quotes.txt") as file:
    quotes = file.readlines()
    quote = random.choice(quotes)

# Send email
with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(my_email, password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs=recipient_list,
        msg=f"Subject: Daily Motivation\n\n{quote}"
    )
