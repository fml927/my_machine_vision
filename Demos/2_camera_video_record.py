# please setting raspPI for open camera first
import picamera
import time

# create & init
camera = picamera.PiCamera()

#setting 
camera.hflip = True
camera.vflip = True

# full screen preview
camera.start_preview()

# start record
camera.start_recording('./output/video_camera.h264')
time.sleep(5)

# end record
camera.stop_recording()

#close preview
camera.close()

