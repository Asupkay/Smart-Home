#!/usr/bin/python

""" These functions are used to convert the photo taken on the pi into base64
and send to our API at https://6ulp.com/predict which sends to Google to analyze
and return a confidence score associated with a person's name """

# Import libraries
import base64
import requests
import paramiko
import os
from time import sleep, time


def convert_photo(link):
    """ Using the base64 class, open a binary file in read-only mode, 
    encode, and return the base64 image """
    image = open(link, "rb") #Open binary file in read-only mode
    image_read = image.read()
    image_base64 = base64.b64encode(image_read)

    return image_base64


def send_image(image_base64):
    """ Using the requests library, send the base64 image in a JSON object
    to our API at https://6ulp.com/predict and print out reponse """
    url = "https://6ulp.com/predict"
    data = image_base64
    files = {"photo": { "base64": data.decode('utf-8')}}

    try:
        r = requests.post(url, json=files)
    except requests.exceptions.RequestException as e:
        print(e)

    with open('/home/pi/Desktop/somefile.txt', 'w') as the_file:
        the_file.write(r.text)
    print(r.text)


def put_to_server(local_path, remote_path):
    """ Using the paramiko library, send an image from a local directory to
    a remote directory through an SSH connection """
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect('server', username='username', password='password')
    except paramiko.SSHException:
        print("Connection Failed")
        quit()

    ftp_client = ssh.open_sftp()
    ftp_client.put(local_path, remote_path)
    ftp_client.close()
    ssh.close()

# Dummy code to illustrate how it works
# image = convert_photo("/Users/Rozanitis/Desktop/pics/person1540333080.335325.jpg")
# image = convert_photo("/home/pi/Desktop/pic_box/person1540333080.335325.jpg")
# send_image(image)

# put_to_server("/Users/Rozanitis/Desktop/pics/person1540333080.33604.jpg", "/home/krozanit/Desktop/dir/person1540333080.33604.jpg")