import smtplib
import datetime as dt
import random
import os
import pandas

# Get environment variables
my_email = os.environ.get("EMAIL_ADDRESS")
password = os.environ.get("EMAIL_PASSWORD")
recipients = os.environ.get("RECIPIENTS")

# Convert comma separated string to list
recipient_list = recipients.split(",")

# Get current day
now = dt.datetime.now()
weekday = now.weekday()

# Send email only on Monday (0 = Monday)
if weekday == 0:

    # Read quotes file
    with open("quotes.txt", "r") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    # Connect to Gmail SMTP
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(my_email, password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=recipient_list,
            msg=f"Subject: Monday Motivation!\n\n{quote}"
        )

    print("Email sent successfully!")
else:
    print("Today is not Monday. No email sent.")
