#!/bin/sh
""" Script to monitor the changes in the directory, pic_box. Whenever
the folder detects that an image was saved to this folder, the program
converts the image to base64 and sends to backend API. After receiving
a JSON response from AutoML with the suggested person and a confidence
interval, this script runs a specific python package on another laptop
to display preferences for the user. """

DIR="/home/krozanit/Desktop/pic_box"
inotifywait -m -r -e create "$DIR" | while read f

do
    echo monkey
    python server.py
done
