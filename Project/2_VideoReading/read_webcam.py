"""
Reading from webcam
"""

# Import Library
import cv2 as cv
import numpy as np

# Read from webcam with video capture
# 0 is the first webcam available
video = cv.VideoCapture(0)

while True:
    check,frame = video.read()
    # Display in color
    cv.imshow('Capture', frame)
    # Display in gray scale
    # Note: OpenCV's color format is BGR
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    cv.imshow('Grey', gray)
    key = cv.waitKey(1)
    # quit with pressing "q"
    if key==ord('q'):
        break

video.release()
cv.destroyAllWindows()