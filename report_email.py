#!/usr/bin/env python3

import os
import datetime
import reports
import emails

# get the current time in GMT
current_date = datetime.datetime.now().strftime('%Y-%m-%d')

def generate_pdf(path):
    pdf = ""
    files = os.listdir(path)
    for file in files:
        if file.endswith(".txt"):
            with open(path + file, 'r') as f:
                inline = f.readlines()
                name = inline[0].strip()
                weight = inline[1].strip()
                pdf += "name: " + name + "<br/>" + "weight: " + weight + "<br/>" + "<br/>"
    return pdf


if __name__ == "__main__":
    user = os.getenv('USER')
    path = "/home/{}/supplier-data/descriptions/".format(user)
    title = "Process Updated on " + current_date
    # generate the package for pdf body
    package = generate_pdf(path)
    reports.generate_report("/tmp/processed.pdf", title, package)

    sender = "automation@example.com"
    receiver = "{}@example.com".format(user)
    subject = "Upload Completed - Online Fruit Store"
    body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."
    attachment = "/tmp/processed.pdf"

    # generate email for the online fruit store report and pdf attachment
    message = emails.generate_email(sender, receiver, subject, body, attachment)
    emails.send_email(message)


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

