"""
Reading video (beautiful.mp4)
"""

# Import Library
import cv2 as cv
import numpy as np
import os

# Absolute path to read
abs_path = os.path.dirname(os.path.dirname(__file__))
gif_path = os.path.join(abs_path, 'input/video/beautiful.mp4')

# Read a gif with video capture
video = cv.VideoCapture(gif_path)

frame_counter = 0

while True:
    check,frame = video.read()
    frame_counter += 1
    resize_frame = cv.resize(frame, (int(frame.shape[1]/2),int(frame.shape[0]/2)))
    cv.imshow('Capture',resize_frame)
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