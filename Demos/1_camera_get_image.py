# please setting raspPI for open camera first
import picamera
import time

# create & init
camera = picamera.PiCamera()

#setting 
camera.hflip = True
camera.vflip = True
# get image
camera.capture('./output/pic1.jpg')
print("create pic1 is ok")
# delay 
time.sleep(1)

#setting 
camera.hflip = True
camera.vflip = False
# get image
camera.capture('./output/pic2.jpg')
print("create pic2 is ok")
# delay 
time.sleep(1)

#setting 
camera.hflip = False
camera.vflip = True
# get image
camera.capture('./output/pic3.jpg')
print("create pic3 is ok")
# delay 
time.sleep(1)

#setting 
camera.hflip = False
camera.vflip = False
# get image
camera.capture('./output/pic4.jpg')
print("create pic4 is ok")
# delay 
time.sleep(1)

#setting 
camera.hflip = True
camera.vflip = True
# get image
camera.capture('./output/pic5.jpg')
print("create pic5 is ok")

#close
camera.close()
print("completed all.")
