# Check Server Health

# Script named health_check.py that will run in the background monitoring some of your system statistics:
# CPU usage, disk space, available memory and name resolution.
# Moreover, this Python script should send an email if there are problems, such as:
# • Report an error if CPU usage is over 80%
# • Report an error if available disk space is lower than 20%
# • Report an error if available memory is less than 500MB
# • Report an error if the hostname "localhost" cannot be resolved to "127.0.0.1"
#
# Complete the script to check the system statistics every 60 seconds,
# and in event of any issues detected among the ones mentioned above, an email should be sent with the following content:
# • From: automation@example.com
# • To: username@example.com
# • Replace username with the username given in the Connection Details Panel on the right hand side.
# • Subject line:

#     ***   Case  ***                                            ***   	Subject line    ***
#  CPU usage is over 80% 	                                   Error - CPU usage is over 80%
#  Available disk space is lower than 20% 	                   Error - Available disk space is less than 20%
#  available memory is less than 500MB 	                       Error - Available memory is less than 500MB
#  hostname "localhost" cannot be resolved to "127.0.0.1" 	   Error - localhost cannot be resolved to 127.0.0.1

# • E-mail Body: Please check your system and resolve the issue as soon as possible.
# Note: There is no attachment file here, so you must be careful while defining the generate_email()
# method in the emails.py script or you can create a separate generate_error_report()
# method for handling non-attachment email. Next, go to the webmail inbox and refresh it.
# There should only be an email something goes wrong, so hopefully you don't see a new email.

# NOTE: You can test the health_check script by using stress module as below:
#
#             import stress
#             stress --cpu 8
#             Allow the stress test to run, as it will maximize our CPU utilization. Now run health_check.py by opening another SSH connection to the linux-instance. It will result in an email sent to the webmail inbox. Its content is as below: Subject: "Error - CPU usage is over 80%" Body: "Please check your system and resolve the issue as soon as possible"
#
# Close the stress --cpu command by clicking Ctrl-c. Now, you will be setting a cron job that executes the script health_check.py every 60 seconds and sends health status to the respective user. To set a user cron job use the following command:
#
#             crontab -e


#!/usr/bin/env python3

import socket
import shutil
import psutil
import emails
import os

