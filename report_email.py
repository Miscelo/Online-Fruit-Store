# send Email with attached pdf

# Once the PDF is generated, you need to send the email using the
#         emails.generate_email() and emails.send_email()    methods from emails.py- file.

# Define generate_email and send_email methods by importing necessary libraries.
# Use the following details to pass the parameters to emails.generate_email():
# • From: automation@example.com
# • To: username@example.com
# • Replace username with the username given in the Connection Details Panel on the right hand side.
# • Subject line: Upload Completed - Online Fruit Store
# • E-mail Body: All fruits are uploaded to our website successfully. A detailed list is attached to this email.
# • Attachment: Attach the path to the file processed.pdf


#!/usr/bin/env python3

import datetime
import os
from reports import generate_report
from emails import generate_email, send_email

def pdf_body():
    return 0

if __name__ == "__main__":
    user = os.getenv('USER')
    # The directory which contains all the files with data in it
    description_directory = '/home/{}/supplier- data/descriptions/'.format(user)