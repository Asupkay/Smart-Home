from picture import Camera
import time
import datetime

flag = 0
last_recorded_capture = datetime.datetime.now()

while True:
    if flag == 0:
        cm = Camera()
        flag = 1
        last_recorded_capture = datetime.datetime.now()
        cm.take_picture()
        delta_value = (datetime.datetime.now() - last_recorded_capture)
    else:
        delta_value = (datetime.datetime.now() - last_recorded_capture)
        if delta_value.seconds > 3:
            cm.close_camera()
            cm = None
            flag = 0
            print("Camera Closed")
            break
            
