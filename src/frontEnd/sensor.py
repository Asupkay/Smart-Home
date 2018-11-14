import RPi.GPIO as GPIO
import time
import datetime
from picture import Camera
import subprocess

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN)

try:
    time.sleep(2)
    # cm = Camera()
    while True:
        # if cm is None:
        #     cm = Camera()
        if GPIO.input(4):
            last_recorded_capture = datetime.datetime.now()
            print(last_recorded_capture)
            # cm.take_picture()
            subprocess.Popen("ssh pi@ipaddress python /home/pi/Desktop/camera.py", shell=True)
            print("\n Motion Detected - Picture Taken")
            print(datetime.datetime.now())
            delta_value = (datetime.datetime.now() - last_recorded_capture)
            print(delta_value.seconds)
        else:
            try:
                print(datetime.datetime.now())
                print("No motion")
                delta_value = (datetime.datetime.now() - last_recorded_capture)
                print(delta_value.seconds)
                if delta_value.seconds > 3:
                    print("Camera Closed")
                # cm.close_camera()
                # cm= None
            except:
                print("Error")
        time.sleep(3)

except Exception as e:
    print(e)
    GPIO.cleanup()
