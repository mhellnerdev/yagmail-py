import yagmail
import os
import time
from datetime import datetime as dt

# define variables to pass to yagmail
sender = 'asdf@asdf.com'
receiver = 'asdf@asdf.com'
subject = "This is the subject"
contents = "Here is a test email contents."

# auth with sender email. must create app password and put in env variables of local machine
yag = yagmail.SMTP(user=sender, password=os.getenv('PASSWORD'))

# function to send mail
def send_mail():
  yag.send(to=receiver, subject=subject, contents=contents)

# loop to send mail on an interval of 60 seconds
# while True:
#   send_mail()
#   print('Email Sent!')
#   time.sleep(60)


# send email at a specific hour and minute every 24 hours
while True:
  now = dt.now()
  if now.hour == 2 and now.minute == 43:
    send_mail()
    print('Email Sent!')
    time.sleep(60)
