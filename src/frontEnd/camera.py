from picture import Camera
import time
import datetime

cm = Camera()

while True:
    if cm is None:
        cm = Camera()
        last_recorded_capture = datetime.datetime.now()
        cm.take_picture()
        delta_value = (datetime.datetime.now() - last_recorded_capture)
    else:
        delta_value = (datetime.datetime.now() - last_recorded_capture)
        if delta_value.seconds > 3:
            cm.close_camera()
            cm = None
            print("Camera Closed")