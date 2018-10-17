from picamera import PiCamera
from time import sleep, time

class Camera:

    def __init__(self):
        self.camera = PiCamera()
        self.camera.start_preview()



    def take_picture(self):
        
        sleep(1)
        self.camera.capture('/home/pi/Desktop/pic_box/'+'picture'+str(time())+'.jpg')
        sleep(1)
        

    def close_camera(self):
        self.camera.stop_preview()
        self.camera.close()
    
#take_picture()
