# Import libraries
import base64
import requests
import os
from helper_functions import convert_photo, send_image
from TensorFlow import TensorDetection

# Run CNN script
raw_image = TensorDetection.tensor_script()

image = convert_photo(raw_image)
send_image(image)


# For when we decide to delete files
# try:
#     os.remove(raw_image)
# except OSError as e:  ## if failed, report it back to the user ##
#     print ("Error: %s - %s." % (e.filename, e.strerror))