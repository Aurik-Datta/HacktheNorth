#Image Detection Of Potholes
from picamera import PiCamera
from time import sleep

camera = PiCamera()

camera.start_preview()
sleep(5)
camera.capture('/home/pi/Desktop/binny/image.jpg')
camera.stop_preview()
