import RPi.GPIO as GPIO
import time
import datetime
from picture import Camera

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN)

try:
    time.sleep(2)
    cm = Camera()
    while True:
        if cm is None:
            cm = Camera()
        if GPIO.input(4):
            last_recorded_capture = datetime.datetime.now()
            print(last_recorded_capture)
            cm.take_picture()
            print("Motion Detected")
            print(datetime.datetime.now())
            delta_value = (datetime.datetime.now() - last_recorded_capture)
            print(delta_value.seconds)
        else:
            print(datetime.datetime.now())
            print("No motion")
            delta_value = (datetime.datetime.now() - last_recorded_capture)
            print(delta_value.seconds)
            if delta_value.seconds > 3:
                cm.close_camera()
                cm= None
        time.sleep(0.1)

except Exception as e:
    print(e)
    GPIO.cleanup()
