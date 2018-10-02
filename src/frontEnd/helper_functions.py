import base64
import requests


def convert_photo(link):
    image = open(link, "rb") #Open binary file in read-only mode
    image_read = image.read()
    image_base64 = base64.encodestring(image_read)

    return image_base64

def send_image(image_base64):
    url = "http://127.0.0.1"
    data = image_base64
    files = {"file": data}

    try:
        r = requests.post(url, files=files)
    except requests.exceptions.RequestException as e:
        print(e)
