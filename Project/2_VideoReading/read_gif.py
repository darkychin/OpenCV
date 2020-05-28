"""
Reading gif (lawnmover.gif)
"""

# Import Library
import cv2 as cv
import numpy as np
import os

# Absolute path to read
abs_path = os.path.dirname(os.path.dirname(__file__))
gif_path = os.path.join(abs_path, 'input/gif/lawnmover.gif')

# Read a gif with video capture
gif = cv.VideoCapture(gif_path)

frame_counter = 0

while True:
    check,frame = gif.read()
    frame_counter += 1
    cv.imshow('Capture',frame)
    if frame_counter==gif.get(cv.CAP_PROP_FRAME_COUNT):
        frame_counter = 0
        gif.set(cv.CAP_PROP_POS_FRAMES, 0)
    # capture a  key in every 25 millisecond, also helps to slow down the frames
    key = cv.waitKey(25)
    # quit with pressing "q"
    if key==ord('q'):
        break
# Looping video reference
# https://stackoverflow.com/questions/10057234/opencv-how-to-restart-a-video-when-it-finishes/19009639

gif.release()
cv.destroyAllWindows()