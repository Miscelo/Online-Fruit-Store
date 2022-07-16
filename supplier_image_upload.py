# mod images and upload them to the fruit catalog

# supplier_image_uplaod
# You have modified the fruit images through changeImage.py script.
# Now, you will have to upload these modified images to the web server that is handling the fruit catalog.
# To do that, you'll have to use the Python requests module to send the file contents to the
# [linux-instance-IP-Address]/upload URL.
# Copy the external IP address of your instance from the Connection Details Panel on the left side and
# enter the IP address in a new web browser tab.
# This opens a web page displaying the text "Fruit Catalog".
# you are going to write a script named supplier_image_upload.py
# that takes the jpeg images from the supplier-data/images directory that you've processed previously
# and uploads them to the web server fruit catalog.

#!/usr/bin/env python3

import requests
import os

external_ip = "localhost"
url = "http://{}/upload/".format(external_ip)
user = os.getenv('USER')
img_dir = '/home/{}/pro/python/pycharmDebian/FinalProject/Online-Fruit-Store/supplier-data/images/'.format(user)

pictures = os.listdir(img_dir)
for picture in pictures:
    if picture.endswith('jpg'):
        with open(img_dir + picture, 'rb') as img_binary:
            r = requests.post(url, files={'file': img_binary})
        if r.status_code == 200:
            print("Picture \'{}\' uploaded to server {}.".format(picture, external_ip))
        else:
            print(r.content)
            print("Image \'{}\' could not be uploaded to the server!".format(picture))


