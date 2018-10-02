import base64
import requests


def convert_photo(link):
    image = open(link, "rb") #Open binary file in read-only mode
    image_read = image.read()
    image_base64 = base64.encodestring(image_read)

    return image_base64

def send_image(image_base64):
    url = "https://clamflelmo.com"
    data = image_base64
    files = {"photo": { "base64": data}}

    try:
        r = requests.post(url, data=files)
    except requests.exceptions.RequestException as e:
        print(e)

    print(r)
