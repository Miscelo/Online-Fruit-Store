#!/usr/bin/env python3

import os
from PIL import Image

user = os.getenv('USER')
img_dir = '/home/{}/supplier-data/images/'.format(user)
pictures = os.listdir(img_dir)

for picture in pictures:
    if 'tiff' in picture and not picture.startswith('.'):
        img_without_extension = os.path.splitext(picture)[0]
        img_jpg = img_dir + img_without_extension + ".jpeg"
        try:
            with Image.open(img_dir + picture) as pic:
                pic.convert('RGB').resize((600, 400)).save(img_jpg, 'JPEG')
        except Exception:
            print("Failed to convert image to jpg!")
        finally:
            print("Image converted to jpg with size 600x400 successfully!!!")



# Script will process the supllier images using PIL module
# Script will process the supllier images using PIL module
# In this section, you will write a Python script named 'changeImage.py' to process the supplier images.
# You will be using the PIL library to update all images within
# ~/supplier-data/images directory to the following specifications:

# • Size: Change image resolution from 3000x2000 to 600x400 pixel
# • Format: Change image format from .TIFF to .JPEG
# After processing the images, save them in the same path ~/supplier-data/images, with a JPEG extension.

# In this section, you will write a Python script named 'changeImage.py' to process the supplier images.
# You will be using the PIL library to update all images within
# ~/supplier-data/images directory to the following specifications:

# • Size: Change image resolution from 3000x2000 to 600x400 pixel
# • Format: Change image format from .TIFF to .JPEG
# After processing the images, save them in the same path ~/supplier-data/images, with a JPEG extension.

