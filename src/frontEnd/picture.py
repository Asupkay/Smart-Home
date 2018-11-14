from picamera import PiCamera
from helper_functions import put_to_server
from time import sleep, time
import os

class Camera:

    def __init__(self):
        self.camera = PiCamera()
        self.camera.start_preview()



    def take_picture(self):
        
        sleep(1)
        image_name = 'picture'+str(time())+'.jpg'
        image_path = '/home/pi/Desktop/pic_box/'+image_name
        self.camera.capture(image_path)
        put_to_server(image_path, '/home/krozanit/Desktop/pic_box/'+image_name, 'ipaddress', 'username', 'password')
        try:
            if os.path.isfile(image_path):
                os.unlink(image_path)
        except Exception as e:
            print(e)
        sleep(1)
        

    def close_camera(self):
        self.camera.stop_preview()
        self.camera.close()
    
#cm = Camera()
#cm.take_picture()
