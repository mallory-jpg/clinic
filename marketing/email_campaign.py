import smtplib
import csv
from string import Template

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
import datetime
from email import encoders
import imaplib
import time

CREDENTIALS_USER = <clinic email>
CREDENTIALS_PASS = <clinic pw>
EMAIL_FROM_DEFAULT = <clinic email again>

EMAIL_SUBJECT = "<clinic name> is moving & shaking things up!"
EMAIL_CC_DEFAULT = ""
EMAIL_BCC_DEFAULT = ""

# CONTACTS_FILE = "pt_emails_2020.csv"
CONTACTS_FILE = "Book2.csv"

# Email Template
def getEmailContent(first_name):
    email_content = """
    Hi """+first_name+""",
    <br><br>
    We hope there has not been too much confusion. <clinic name> has moved from our old location on <old location> to 
    <new location>, near the <university name> campus. Once we start seeing patients 
    in person again, please come to our new location!
    <br><br>
    Currently, we continue to operate under COVID-19 protocols which means that all appointments are over the phone
    unless our staff explicitly says otherwise. On the day of your appointment, we will give you a call about 15 minutes
    before your scheduled time. Once we get ahold of you, you will get to talk to your provider and ask any questions
    you may have. If you are due for any labs, we will send you to one of the labs we contract with, and we will find the
    location nearest to you!
    <br><br>
    If you have any questions about this, please feel free to give us a call at 512-467-0088. 
    <br><br>
    Thank you kindly,<br>
    Mallory Culbert
    """
    return email_content

def loop_contacts(filename):
    print("Looping contacts")

    print("Sending emails")
    s = smtplib.SMTP(host="smtp.office365.com", port=587)
    s.starttls()
    s.login(CREDENTIALS_USER, CREDENTIALS_PASS)

    count = 1

    with open(filename, mode="r") as contacts_file:
        reader = csv.reader(contacts_file)
        next(reader)
        for contact in reader:
            contact_full_name = contact[0]
            email = contact[1]
            # first_name = contact[1]

            msg = MIMEMultipart()

            print(count)
            count = count+1
            print("Sending email to", contact_full_name)

            msg["From"] = EMAIL_FROM_DEFAULT
            msg["To"] = email
            msg["Bcc"] = EMAIL_BCC_DEFAULT
            msg["Subject"] = EMAIL_SUBJECT

            msg.attach(MIMEText(getEmailContent(contact_full_name), "html"))
            print(type(msg))
            s.send_message(msg)

            del msg

    s.quit()

loop_contacts(CONTACTS_FILE)
