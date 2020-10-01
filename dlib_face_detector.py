from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
import dlib

width, Height = 320, 240

#face detector
detector = dlib.get_frontal_face_detector()


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
    faces = detector(GRAY)
    for face in faces:
        x, y =face.left(), face.top()
        x1, y1 = face.right(), face.bottom()
        cv2.rectangle(image, (x, y), (x1, y1), (0, 255, 0), 2)
    #cv2.imshow('image', GRAY)
    # show the frame
    cv2.imshow("Frame", image)
    key = cv2.waitKey(1) & 0xFF
    # clear the stream in preparation for the next frame
    rawCapture.truncate(0)
    # if the `q` key was pressed, break from the loop
    if key == ord("q"):
        break


