#!/bin/sh
""" Script to monitor the changes in the shared directory with Pi 1. Whenever
the folder detects that an image was saved to the shared folder, the program
converts the image to base64 and sends to backend API. """

# DIR="/home/krozanit/Desktop/dir"
DIR="/home/pi/Desktop/pic_box"
inotifywait -m -r -e create "$DIR" | while read f

do
    echo monkey
    python server.py
done