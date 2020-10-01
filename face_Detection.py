from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
width, Height = 320, 240

face_Detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

# initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()
camera.resolution = (width, Height)
camera.framerate = 6
rawCapture = PiRGBArray(camera, size=(width, Height))
# allow the camera to warmup

time.sleep(0.1)
# capture frames from the camera
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    # grab the raw NumPy array representing the image, then initialize the timestamp
    # and occupied/unoccupied text
    image = frame.array
    GRAY =cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # detect faces in the grayscale frame
    faces = face_Detector.detectMultiScale(GRAY, scaleFactor=1.1, 
        minNeighbors=5, minSize=(30, 30),flags=cv2.CASCADE_SCALE_IMAGE)
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x,y), (x+w, y+h), (0, 255, 0), 3)
        
    #cv2.imshow('image', GRAY)
    # show the frame
    cv2.imshow("Frame", image)
    key = cv2.waitKey(1) & 0xFF
    # clear the stream in preparation for the next frame
    rawCapture.truncate(0)
    # if the `q` key was pressed, break from the loop
    if key == ord("q"):
        break

