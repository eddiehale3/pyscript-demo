from datetime import datetime
import smtplib
from email.mime.text import MIMEText

def convert_to_fahrenheit(celsius_value):
  return round((celsius_value * 1.8000) + 32.00)

def get_current_time():
  now = datetime.now()
  return now.strftime("%m/%d/%Y, %H:%M")

# def send_email(first, last, subject, message):
#   # Open a plain text file for reading.  For this example, assume that
#   # the text file contains only ASCII characters.
#   # with open(textfile, 'rb') as fp:
#   #     # Create a text/plain message
#   #     msg = MIMEText(fp.read())

#   msg = MIMEText(message)

#   # me == the sender's email address
#   # you == the recipient's email address
#   me = 'no-reply@gmail.com'
#   you = 'eddie.hale@gmail.com'
#   msg['Subject'] = 'The contents of %s' % subject
#   msg['From'] = me
#   msg['To'] = you

#   # Send the message via our own SMTP server, but don't include the
#   # envelope header.
#   s = smtplib.SMTP('localhost')
#   s.sendmail(me, [you], msg.as_string())
#   s.quit()

# send_email('Eddie', 'Hale', 'Test email from laptop', 'Hello world!!')