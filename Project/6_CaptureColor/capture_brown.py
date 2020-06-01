"""
Reading video (beautiful.mp4) and capture a range of brown color only
"""

# Import Library
import cv2 as cv
import numpy as np
import os

# Absolute path to read
abs_path = os.path.dirname(os.path.dirname(__file__))
video_path = os.path.join(abs_path, 'input/video/beautiful.mp4')

# Read a gif with video capture
video = cv.VideoCapture(video_path)

frame_counter = 0

while True:
    # '_' can be used on unused or ignored variable
    _, frame = video.read()
    frame_counter += 1
    resize_frame = cv.resize(frame, (int(frame.shape[1]/2),int(frame.shape[0]/2)))

    # Convert frame color to Hue,Saturation,Value(HSV)
    hsv = cv.cvtColor(resize_frame, cv.COLOR_BGR2HSV)

    # Hsv brown color range we wish to capture
    lower_brown = np.array([0,50,50])
    upper_brown = np.array([40,255,240])

    mask = cv.inRange(hsv, lower_brown, upper_brown)

    result = cv.bitwise_and(resize_frame, resize_frame, mask = mask)

    # Show frame
    cv.imshow('Original', resize_frame)
    cv.imshow('Mask', mask)
    cv.imshow('Result', result)

    if frame_counter==video.get(cv.CAP_PROP_FRAME_COUNT):
        frame_counter = 0
        video.set(cv.CAP_PROP_POS_FRAMES, 0)
    # capture a  key in every 25 millisecond, also helps to slow down the frames
    key = cv.waitKey(25)
    # quit with pressing "q"
    if key==ord('q'):
        break

video.release()
cv.destroyAllWindows()