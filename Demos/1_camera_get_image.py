# please setting raspPI for open camera first
import picamera
import time

# create & init
camera = picamera.PiCamera()

#setting 
camera.hflip = True
camera.vflip = True

# get image
camera.capture('image1.jpg')
time.sleep(1)
camera.capture('image2.jpg')
time.sleep(1)
camera.capture('image3.jpg')
time.sleep(1)
camera.capture('image4.jpg')
time.sleep(1)
camera.capture('image5.jpg')
time.sleep(1)

#close
camera.close()
