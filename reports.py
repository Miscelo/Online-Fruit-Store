# Generate Report , create pdf

# Once the images and descriptions have been uploaded to the fruit store web-server,
# you will have to generate a PDF file to send to the supplier, indicating that the data was correctly processed.
# To generate PDF reports, you can use the ReportLab library. The content of the report should look like this:
# Processed Update on
# [blank line]
# name: Apple
# weight: 500 lbs
# [blank line]
# name: Avocado
# weight: 200 lbs
# [blank line]
# ...
# You will need to pass the following arguments to the reports.generate_report method:
# 1. the text description processed from the text files as the paragraph argument,
# 2. the report title as the title argument,
# 3. and the file path of the PDF to be generated as the attachment argument (use ‘/tmp/processed.pdf')

#!/usr/bin/env python3

from reportlab.platypus import Paragraph, Spacer, Image, SimpleDocTemplate
from reportlab.lib.styles import getSampleStyleSheet


def generate_report(file, title, add_info):
    styles = getSampleStyleSheet()
    report = SimpleDocTemplate(file)
    report_title = Paragraph(title, styles['h1'])
    report_info = Paragraph(add_info, styles['BodyText'])
    empty_line = Spacer(1, 20)

    report.build([report_title, empty_line, report_info, empty_line])