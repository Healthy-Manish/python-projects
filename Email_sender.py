#  go over our gmail account and setup 2 factor authentication
# generate app password
#  create a function to send the mail

from email.message import EmailMessage
from app2 import password
import ssl
import smtplib

email_sender = 'manishdwivedi45165@gmail.com'
email_password = password

email_reciever = 'manishdwivedi7060@gmail.com'
subject = "Don't forget  to have dinner"
body = """
When you reach home , please have dinner
"""

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_reciever
em['subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
    smtp.login(email_sender,email_password)
    smtp.sendmail(email_sender,email_reciever,em.as_string())
