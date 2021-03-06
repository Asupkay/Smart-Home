# Import libraries
import base64
import requests
import os
from helper_functions import convert_photo, send_image, parsejson
import TensorDetection

# Run CNN script
raw_image = TensorDetection.tensor_script()

if raw_image == True:
    for img in os.listdir('/home/krozanit/Desktop/box'):
        print(img)
        image = convert_photo('/home/krozanit/Desktop/box/'+img)
        username = send_image(image)
        parsejson(username)
        try:
            if os.path.isfile('/home/krozanit/Desktop/box/'+img):
                os.unlink('/home/krozanit/Desktop/box/'+img)
        except Exception as e:
            print(e)



# For when we decide to delete files
# try:
#     os.remove(raw_image)
# except OSError as e:  ## if failed, report it back to the user ##
#     print ("Error: %s - %s." % (e.filename, e.strerror))
